import json

def read_json(path_to_file: str) -> str:
    with open(path_to_file, 'r', encoding="utf-8") as file:        
        try:   
            json_data = json.load(file)         
            return json_data
        except KeyError:
            return None

