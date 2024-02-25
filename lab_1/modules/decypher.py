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

def get_key(dict1: dict, dict2: dict)->dict:
    encryption_key = {}
    keys_list = list(dict2.keys())
    for key1 in dict1.keys():
        if keys_list:
            key2 = keys_list.pop(0)
            encryption_key[key2] = key1
    return encryption_key

def decrypt_by_key(cypher: str, key: dict)->str:
    decrypted_text = ""
    for symbol in cypher:
        decrypted_text = cypher.replace(symbol, key[symbol])
    return decrypted_text
