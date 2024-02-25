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
        
def frequency_analysis(text: str) -> dict:
    frequency = {}
    lenght = len(text)
    for symbol in text:
        if symbol in frequency:
            frequency[symbol] += 1 / lenght
        else:
            frequency[symbol] = 1 / lenght
    
    return dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))

