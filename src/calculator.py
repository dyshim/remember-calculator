import re
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import operator

form_class = uic.loadUiType('./calculator.ui')[0]  # UI 파일(XML)을 파이썬 코드로 불러오기


def typeCasting(obj):
    if obj == int(obj):
        return int(obj)

    return obj


class Form(QWidget, form_class):
    def __init__(self):
        super(Form, self).__init__()
        self.setupUi(self)

        # Setup numbers
        for n in range(0, 10):
            getattr(self, 'btn_%s' % n).pressed.connect(lambda v=n: self.inputNumber(v))

        self.btn_point.pressed.connect(self.inputDecimalPoint)

        # Setup operations
        self.btn_add.pressed.connect(lambda: self.operation(operator.add))
        self.btn_sub.pressed.connect(lambda: self.operation(operator.sub))
        self.btn_mul.pressed.connect(lambda: self.operation(operator.mul))
        self.btn_div.pressed.connect(lambda: self.operation(operator.truediv))

        self.btn_equals.pressed.connect(self.equals)

        self.btn_back.pressed.connect(self.backDelete)
        self.btn_clear.pressed.connect(self.clear)
        self.btn_reset.pressed.connect(self.reset)

        self.reset()
        self.history = list()

    def reset(self):
        self.switchButtonState(True)
        self.inputOK = False  # 숫자 입력 상태 Flag.
        self.current_op = None
        self.stack = [0]
        self.mathExpr = list()  # 수식 표현 리스트

        self.lbl_expr.clear()
        self.lbl_display.setText("0")

        self.display(str(self.stack[-1]))

    def inputNumber(self, v):
        # 입력값 처리 -> 최대 11자리까지 입력 가능. (소수점 포함)
        lbl = self.lbl_display
        text = lbl.text().replace(",", "")

        if text == "inf":
            self.reset()

        if not self.inputOK or text == "0":
            self.inputOK = True
            text = ""

        if self.inputOK:
            if len(text) < 10:
                self.display(text + str(v))

    def display(self, text):
        # 화면에 결과 출력
        self.lbl_display.setText(self.insertComma(text))
        self.lbl_expr.setText(" ".join(str(i) for i in self.mathExpr))

        if text != "inf":
            self.stack[-1] = eval(text)

    def insertComma(self, str_v):
        # 3자리 마다 콤마(,) 삽입
        regex = r'(?<=\d)(?=(\d{3})+(?!\d))'
        if '.' in str_v:
            return self.insertComma(str_v[:str_v.find('.')]) + str_v[str_v.find('.'):]
        else:
            return re.sub(regex, ',', str_v)

    def inputDecimalPoint(self):
        if not self.inputOK:
            self.inputOK = True
            self.stack[-1] = 0

        if '.' not in str(self.stack[-1]):
            self.display(str(self.stack[-1]) + ".")

    def getDisplayValue(self):
        return typeCasting(eval(self.lbl_display.text().replace(",", "")))

    def operation(self, op):
        # 연산자 처리
        self.stack[-1] = self.getDisplayValue()
        # print(f"Stack state {self.stack} \nCurrent stack value type {type(self.stack[-1])}")

        if self.inputOK:
            self.inputOK = False
            if self.current_op:
                self.equals()

        self.current_op = op
        self.mathExpr = [self.stack[0], self.sender().text()]

        self.display(str(self.stack[-1]))

        if len(self.stack) < 2:
            self.stack.append(0)

    def equals(self):
        self.stack[-1] = self.getDisplayValue()
        self.mathExpr += [self.stack[-1], "="]

        if self.current_op:
            try:
                print(f"==== 연산 START! ====")
                result = self.current_op(*self.stack)
                print(f"{self.stack} \n"
                      f"연산 결과: {round(result, 8)}")
                self.stack = [typeCasting(round(result, 8))]
            except ZeroDivisionError:
                print("ZeroDivisionError")
                self.stack[-1] = float("inf")
                self.switchButtonState(False)

        self.display(str(self.stack[-1]))

        self.mathExpr.append(self.stack[-1])
        self.history.append(self.mathExpr.copy())
        print(f"3 Recent Records History: {self.history[::-1][:3]}")

        self.inputOK = False
        self.current_op = None
        self.mathExpr.clear()

    def switchButtonState(self, stat):
        # Infinity 입력 시 버튼 상태 변경
        buttons = ['add', 'sub', 'mul',
                   'div', 'point', 'equals']

        for item in buttons:
            getattr(self, 'btn_%s' % item).setEnabled(stat)

    def backDelete(self):
        # Backspace 처리
        lbl = self.lbl_display
        text = lbl.text().replace(",", "")

        if self.inputOK:
            if len(lbl.text()) == 1:
                self.display("0")
            else:
                self.display(text[:-1])
        else:
            if text == "inf":
                self.reset()

        if not self.mathExpr:
            self.lbl_expr.clear()

    def clear(self):
        self.switchButtonState(True)
        self.stack[-1] = 0

        if not self.mathExpr:
            self.lbl_expr.clear()

        if self.lbl_display.text() == "inf":
            self.reset()

        self.display(str(self.stack[-1]))

    def closeEvent(self, QCloseEvent):
        # 창 닫기
        ans = QMessageBox.question(self, '종료하기', '종료하시겠습니까?',
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainForm = Form()
    mainForm.show()
    sys.exit(app.exec_())  # 이벤트 루프
