import multiprocessing as mp
from matplotlib import pyplot as plt
import hashlib as hl

from modules import work_with_files

def generate_card_number(bins: list, guessed_digits: int, last_digit: str)->str:
    return f'{bin}{str(guessed_digits).zfill(6)}{last_digit}'


def comparing_card_with_hash(card_number: str, hash: str)->bool:
    return hl.sha224(card_number.encode()).hexdigest() == hash


def select_card_number(hash: str, last_digits: int, bins: list)->str:    
    with mp.Pool(processes=mp.cpu_count()) as p:
        for res in p.map(select_card_number, [(i, last_digits, hash) for i in range(0, 999999)]):
            if res:                
                work_with_files.writing_to_json(res, "output_data/card_number.json")
                print(f"Мы нашли {res} при количестве: {mp.cpu_count()} процессов и закрыли пул")
                p.terminate()
                return res
            

def algorithm_Luna(card_number: str)->bool:
    pass

