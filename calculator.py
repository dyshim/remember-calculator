import re
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from mylib import float_to_int, export_history

import operator

form_class = uic.loadUiType('./calculator.ui')[0]  # UI 파일(XML)을 파이썬 코드로 불러오기


class Form(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.initUI()

        self.reset()
        self.history = list()

    def initUI(self):
        # Setup numbers
        for n in range(0, 10):
            getattr(self, "btn_%s" % n).pressed.connect(self.setInputNumberValue)

        # Setup operations
        self.btn_add.pressed.connect(lambda: self.operation(operator.add))
        self.btn_sub.pressed.connect(lambda: self.operation(operator.sub))
        self.btn_mul.pressed.connect(lambda: self.operation(operator.mul))
        self.btn_div.pressed.connect(lambda: self.operation(operator.truediv))

        self.btn_equal.pressed.connect(self.equals)

        self.btn_del.pressed.connect(self.backDelete)
        self.btn_clear.pressed.connect(self.clear)
        self.btn_reset.pressed.connect(self.reset)
        self.btn_point.pressed.connect(self.setInputDecimalPoint)

        # Change the state of the clicked item -> No selected
        self.listWidget.itemSelectionChanged.connect(lambda: self.listWidget.currentItem().setSelected(False))
        self.listWidget.itemClicked.connect(self.read_item)
        self.btn_remove.pressed.connect(self.clear_history)
        self.btn_save.clicked.connect(lambda: export_history(self.history[::-1]))

    def reset(self):
        # AC 버튼을 눌렀을 때
        self.buttonStatSwitch(True)
        self.inputOK = False  # 피연산자 입력 상태 확인
        self.current_op = None
        self.stack = [0]
        self.math_exp = list()  # 수식을 담을 리스트

        self.display(str(self.stack[-1]), " ".join(str(v) for v in self.math_exp))

    def setInputNumberValue(self):
        # 숫자 버튼을 입력했을 때
        text = self.lbl_result.text().replace(",", "")

        if text == "inf":
            self.reset()

        if not self.inputOK or text == "0":
            self.inputOK = True
            text = ""

        if self.inputOK:
            # 최대 11자리까지 입력 가능 (소수점 포함)
            if len(text) < 10:
                self.display(text + self.sender().text(), " ".join(str(v) for v in self.math_exp))

    def display(self, text, math_exp):
        # 입력한 값 화면에 출력
        self.lbl_result.setText(str(self.getInsertCommaValue(text)))
        self.lbl_text.setText(math_exp)

        if text != "inf":
            self.stack[-1] = eval(text)

    def getInsertCommaValue(self, text):
        # 3자리 마다 콤마(,) 삽입
        reg = r'(?<=\d)(?=(\d{3})+(?!\d))'
        if "." in text:
            return self.getInsertCommaValue(text[:text.find('.')]) + text[text.find('.'):]
        else:
            return re.sub(reg, ',', text)

    def setInputDecimalPoint(self):
        # '.' 버튼을 입력했을 때
        if not self.inputOK:
            self.inputOK = True
            self.stack[-1] = 0

        if "." not in str(self.stack[-1]):
            self.display(str(self.stack[-1]) + ".", " ".join(str(v) for v in self.math_exp))

    def getDisplayValue(self):
        return float_to_int(eval(self.lbl_result.text().replace(",", "")))

    def operation(self, op_func):
        # 연산자 버튼을 입력했을 때
        self.stack[-1] = self.getDisplayValue()
        # print(f"Stack state {self.stack} \nCurrent stack value type {type(self.stack[-1])}")

        if self.inputOK:
            self.inputOK = False
            if self.current_op:
                self.equals()

        self.current_op = op_func
        self.math_exp = [self.stack[0], self.sender().text()]

        self.display(str(self.stack[-1]), " ".join(str(v) for v in self.math_exp))

        if len(self.stack) < 2:
            self.stack.append(0)

    def equals(self):
        self.stack[-1] = self.getDisplayValue()
        self.math_exp += [self.stack[-1], "="]

        if self.current_op:
            try:
                print(f"===='{self.math_exp[1]}' 연산 START! ====")
                result = self.current_op(*self.stack)
                print(f"Stack: {self.stack} \n"
                      f"연산 결과: {round(result, 8)} \n")
                self.stack = [float_to_int(round(result, 8))]
            except Exception as e:
                if ZeroDivisionError:
                    self.stack[-1] = float("inf")
                self.buttonStatSwitch(False)
                print(f"Error: {e}")

        self.display(str(self.stack[-1]), " ".join(str(v) for v in self.math_exp))

        self.math_exp.append(self.stack[-1])
        self.history.append(self.math_exp.copy())
        # print(f"3 Recent Records History: {self.history[::-1][:3]}")

        self.add_to_listWidget(self.history[-1])

        self.inputOK = False
        self.current_op = None
        self.math_exp.clear()

    def add_to_listWidget(self, lst):
        # 계산 수식 listWidget 에 넣기
        self.btn_remove.setEnabled(True)  # 휴지통 활성화
        self.btn_save.setEnabled(True)  # 저장 활성화

        items = list()

        # 기존 모든 item 을 리스트에 담기
        if self.listWidget.count():
            items = [self.listWidget.item(i) for i in range(self.listWidget.count())]
            """
            items: List QListWidgetItem object id 
            """

        text = " ".join(str(v) for v in lst[:-1])
        self._add_item(f"{text}\n{lst[-1]}")

        for item in items:
            row = self.listWidget.row(item)
            self.listWidget.takeItem(row)

            self._add_item(item.text())

    def _add_item(self, text):
        item = QListWidgetItem(text)
        item.setTextAlignment(Qt.AlignRight)
        item.setFont(QtGui.QFont("나눔고딕", 13, QFont.Bold))
        self.listWidget.addItem(item)

    def read_item(self):
        # 클릭한 item 값 가져오기
        text = self.listWidget.currentItem().text()
        math_exp, result = text.split("\n")

        self.display(result.strip(), math_exp.strip())

    def clear_history(self):
        # 모든 기록 지우기
        self.listWidget.clear()
        self.history.clear()
        self.btn_remove.setEnabled(False)
        self.btn_save.setEnabled(False)

    def buttonStatSwitch(self, stat):
        # 예외 발생 시, 버튼 상태 변경
        buttons = ['add', 'sub', 'mul',
                   'div', 'point', 'equal']

        for item in buttons:
            getattr(self, 'btn_%s' % item).setEnabled(stat)

    def backDelete(self):
        # Backspace 버튼 처리
        lbl = self.lbl_result
        text = lbl.text().replace(",", "")
        math_exp = " ".join(str(v) for v in self.math_exp)

        if self.inputOK:
            if len(lbl.text()) == 1:
                self.display("0", math_exp)
            else:
                self.display(text[:-1], math_exp)
        else:
            if text == "inf":
                self.reset()

        if not self.math_exp:
            self.lbl_text.clear()

    def clear(self):
        # C 버튼을 입력했을 때
        if self.lbl_result.text() == "inf":
            self.reset()

        self.display("0", " ".join(str(v) for v in self.math_exp))

    def closeEvent(self, QCloseEvent):
        # 창 닫기
        ans = QMessageBox.question(self, '종료하기', '종료하시겠습니까?', QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    winForm = Form()
    winForm.show()
    sys.exit(app.exec_())  # 이벤트 루프
