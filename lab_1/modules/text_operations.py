import os
import json
def read_text(path: str) -> str :
    text = ""
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def write_file(path: str, text: str) -> None:            
    with open(path, 'a', encoding='utf-8') as file:
        file.write(text)

def write_dict_to_json(path: str, data: dict)->None:    
    with open(path, 'a', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)
        file.write('\n')

    

def read_json(path: str)->dict:
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)