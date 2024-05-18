import json
import logging


def writing_to_json(data: dict, path: str) -> None:
    """
    Writes the given data to a JSON file at the specified path.

    Args:
        data (dict): The data to be written to the JSON file.
        path (str): The path to the JSON file.

    Raises:
        Exception: If an error occurs while writing to the file.
    """
    try:
        with open(path, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        logging.error(f"[writing_to_json]: {e}")


def read_json(path: str) -> dict:
    """
    Reads and returns the data from a JSON file at the specified path.

    Args:
        path (str): The path to the JSON file.

    Returns:
        dict: The data read from the JSON file.

    Raises:
        Exception: If an error occurs while reading the file.
    """
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except Exception as e:
        logging.error(f"[read_json]: {e}")
        return {}


def read_txt(path: str) -> str:
    """
    Reads and returns the contents of a text file at the specified path.

    Args:
        path (str): The path to the text file.

    Returns:
        str: The contents of the text file.

    Raises:
        Exception: If an error occurs while reading the file.
    """
    try:
        with open(path, 'r') as file:
            return file.read()
    except Exception as e:
        logging.error(f'[read_txt]: {e}')
        return ''