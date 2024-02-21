import os
import json
def read_text(path: str | None, filename: str) -> str :
    current_dir = os.getcwd()
    if path != None:    
        os.chdir(path)
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    os.chdir(current_dir)

    return text

def write_file(path: str, text: str) -> None:            
    with open(path, 'a', encoding='utf-8') as file:
        file.write(text)

def write_to_json(path: str, data: dict)->None:    
    with open(path, 'a', encoding='utf-8') as file:
        json.dump(data, file)
    

def read_json(path: str)->dict:
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)