from modules.additional_functions import *

def decypher_caesar(encrypted_text: str, key: int)->str:
    alphabet = defining_alphabet(encrypted_text)
    decypher = ""
    for symbol in encrypted_text:
        if symbol in alphabet:
            index = (alphabet.index(symbol) - key) % len(alphabet)
            decypher += alphabet[index]
        else:
            decypher += symbol

    return decypher

def decrypt_by_key(cypher: str, key: dict)->str:
    decrypted_text = ""
    for symbol in cypher:
        decrypted_text
