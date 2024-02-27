from modules.additional_functions import *

def decypher_caesar(encrypted_text: str, key: int) -> str:
    '''
    Decrypts the text using the Caesar method using the specified key.
            Parameters:    
                    encrypted_text (str): encrypted text
                    key (int): encryption key                   
            Return value:
                    str: the function returns 
                    the decrypted text as a string
    '''
    alphabet = defining_alphabet(encrypted_text)
    decypher = ""

    for symbol in encrypted_text:
        if symbol in alphabet:
            index = (alphabet.index(symbol) + (len(alphabet) - key)) % len(alphabet)
            decypher += alphabet[index]
        else:
            decypher += symbol

    return decypher

def decrypt_by_key(encrypted_text: str, key: dict) -> str:
    '''
    Decrypts the text by frequency analysis using the specified key.
            Parameters:    
                    encrypted_text (str): encrypted text
                    key (dict): encryption key                   
            Return value:
                    str: the function returns 
                    the decrypted text as a string
    '''
    decr_text = ""
    for symbol in encrypted_text:
        decr_text += symbol.replace(symbol, key[symbol])
    return decr_text
