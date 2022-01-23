from PyQt5.QtWidgets import QFileDialog


def float_to_int(value):
    if float(value) == int(value):
        return int(value)

    return float(value)


def export_history(hisData: list):
    f_name = QFileDialog.getSaveFileName(filter="텍스트 문서(*.txt)")

    if f_name[0]:
        path = f_name[0]

        print(path, hisData)
        _save_to_path(path, hisData)


def _save_to_path(f_path, hisData, sep='\n'):
    with open(f_path, 'w', encoding='UTF-8') as f:
        for data in hisData:
            text = "".join(str(v) for v in data)
            f.write(text + sep)