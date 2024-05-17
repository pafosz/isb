import multiprocessing as mp
from matplotlib import pyplot as plt
import hashlib as hl
import time
import numpy as np

from tqdm import tqdm
from modules import work_with_files


def checking_card_by_hash(bins: list, guessed_digit: int, last_digits: int, hash: str)->str:
    
    for bin in bins:
        guessed_card_number = f'{str(bin)}{str(guessed_digit).zfill(6)}{str(last_digits)}'
        if hl.sha224(guessed_card_number.encode()).hexdigest() == hash:
            return guessed_card_number


def select_card_number(hash: str, last_digits: int, bins: list, count_cpu: int)->str:    
    
    with mp.Pool(count_cpu) as p:              
        for res in p.starmap(checking_card_by_hash, [(bins, i, last_digits, hash) for i in list(range(0, 999999))]):                
            if res:                   
                work_with_files.writing_to_json(res, "card_number.json")
                print(f"Мы нашли {res} при количестве: {count_cpu} процессов и закрыли пул")
                p.terminate()
                return res
            

def algorithm_Luna(card_number: str)->bool:
    reverse_card_number = [int(digit) for digit in card_number[::-1]]
    for i in range(len(reverse_card_number)):
        if i % 2 != 0:
            reverse_card_number[i] *= 2
            if reverse_card_number[i] > 10:
                reverse_card_number[i] = (reverse_card_number[i] % 10) + (reverse_card_number[i] // 10)
    return sum(reverse_card_number) % 10 == 0


def time_to_search_for_collision(hash: str, last_digits: int, bins: list)->None:
    time_list = []
    for count_cpu in tqdm(range(1, int(1.5 * mp.cpu_count())), desc="Поиск коллизии"):
        start = time.time()
        if select_card_number(hash, last_digits, bins, count_cpu):
            time_list.append(time.time() - start)

    x = list(range(1, int(1.5 * mp.cpu_count())))
    y = time_list

    plt.figure(figsize=(30,5))
    plt.xlabel('Количество процессов')
    plt.ylabel('Время выполнения, c')
    plt.title('Зависимость количества процессов от времени')    
    plt.plot(x, y, color='m', linestyle='--', marker='x', linewidth=1, markersize=4)
    plt.show()
