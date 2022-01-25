def float_to_int(value):
    if float(value) == int(value):
        return int(value)

    return float(value)


def save_to_path(f_path, hisData, sep='\n'):
    with open(f_path, 'w', encoding='UTF-8') as f:
        for data in hisData:
            text = "".join(str(v) for v in data)
            f.write(text + sep)