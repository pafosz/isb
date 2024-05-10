import json
import logging

def writing_to_json(data: str, path: str)->None:
    """
    Writes data in JSON format to a file.

    Parameters:
    data (str): The data to be written in JSON format.
    path (str): The file path where the data will be written.

    Returns:
    None
    """
    try:
        with open(path, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        logging.error(f'[writing_to_json]: {e}')


def read_json(path: str)->str:
    """
    Reads data from a JSON file and returns it.

    Parameters:
    path (str): The file path of the JSON file to be read.

    Returns:
    str: The data read from the JSON file.

    """
    try:
        with open(path, 'r') as file:
            data = json.loads(file)

        return data
    except Exception as e:
        logging.error(f'[read_json]: {e}')

    
def write_bytes_to_txt(data: str, path: str)->None:
    """
    Writes data to a text file.

    Parameters:
    data (str): The data to be written to the file.
    path (str): The file path where the data will be written.

    Returns:
    None
    """
    try:
        with open(path, 'wb') as file:
            file.write(data)
    except Exception as e:
        logging.error(f'[write_to_txt]: {e}')

def read_bytes(path: str)->bytes:
    """
    Reads byte data from a file.

    Parameters:
    path (str): The file path to be read.

    Returns:
    bytes: The byte data read from the file.
    """
    try:
        with open(path, 'rb') as file:
            data = file.read()
        return data
    except Exception as e:
        logging.error(f'[read_bytes]: {e}')