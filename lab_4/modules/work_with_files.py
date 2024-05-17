import json
import logging

def writing_to_json(data: dict, path: str)->None:
    try:
        with open(path, 'w') as file:
           json.dump(data, file)
    except Exception as e:
        logging.error(f"[writing_to_json]: {e}")


def read_json(path: str)->dict:
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"[read_json]: {e}")

