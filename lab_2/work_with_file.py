import json

def read_json(path_to_file: str) -> str:
    """
    This function reads and loads JSON data from a file specified by the path.

        Parameters:
            path_to_file (str): The path to the JSON file to read.

        Returns:
            str: The JSON data loaded from the file.
    """
    with open(path_to_file, 'r', encoding="utf-8") as file:        
        try:   
            json_data = json.load(file)         
            return json_data
        except KeyError:
            return None

