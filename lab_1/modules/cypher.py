from modules.additional_functions import *

def сaesar_cypher(text: str, key: int)->str:  
    text = text.upper()
    alphabet = defining_alphabet(text)
   
    cypher = ""
    for symbol in text:
        if symbol in alphabet:
            index = (alphabet.index(symbol) + key) % len(alphabet)
            cypher += alphabet[index]
        else:
            cypher += symbol

    return cypher

    


    
        

    
