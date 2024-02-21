RUS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ENG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def defining_alphabet(text: str)->str:
    for symbol in text:
        if symbol in RUS:
            return RUS
        elif symbol in ENG:
            return ENG
        else:
            raise ValueError('Такого языка я не знаю')