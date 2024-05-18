import hashlib as hl
import multiprocessing as mp
import time
from matplotlib import pyplot as plt
from typing import List, Optional
from tqdm import tqdm

from modules import work_with_files


def checking_card_by_hash(bins: List[int], guessed_digit: int, last_digits: int, hash_value: str) -> Optional[str]:
    """
    Checks if the generated card number matches the given hash.

    Args:
        bins (List[int]): A list of bin numbers.
        guessed_digit (int): The guessed digit to be appended to the bin.
        last_digits (int): The last four digits of the card number.
        hash_value (str): The hash value to compare against.

    Returns:
        Optional[str]: The full card number if a match is found, otherwise None.
    """
    for bin_num in bins:
        guessed_card_number = f'{str(bin_num)}{str(guessed_digit).zfill(6)}{
            str(last_digits)}'
        if hl.sha224(guessed_card_number.encode()).hexdigest() == hash_value:
            return guessed_card_number
    return None


def select_card_number(hash_value: str, last_digits: int, bins: List[int], count_cpu: int) -> Optional[str]:
    """
    Searches for a card number that matches the given hash and last four digits.

    Args:
        hash_value (str): The hash value to search for.
        last_digits (int): The last four digits of the card number.
        bins (List[int]): A list of bin numbers.
        count_cpu (int): The number of CPU processes to use for the search.

    Returns:
        Optional[str]: The found card number, or None if no match is found.
    """
    with mp.Pool(count_cpu) as pool:
        for result in pool.starmap(checking_card_by_hash, [(bins, i, last_digits, hash_value) for i in range(1_000_000)]):
            if result:
                work_with_files.writing_to_json(result, "card_number.json")
                print(f"Found {result} using {
                      count_cpu} processes. Terminating pool.")
                pool.terminate()
                return result
    return None


def algorithm_luna(card_number: str) -> bool:
    """
    Checks if a credit card number is valid using the Luhn algorithm.

    Args:
        card_number (str): The credit card number to check.

    Returns:
        bool: True if the card number is valid, False otherwise.
    """
    reverse_card_number = [int(digit) for digit in card_number[::-1]]
    for i in range(len(reverse_card_number)):
        if i % 2 != 0:
            reverse_card_number[i] *= 2
            if reverse_card_number[i] > 9:
                reverse_card_number[i] = (
                    reverse_card_number[i] % 10) + (reverse_card_number[i] // 10)
    return sum(reverse_card_number) % 10 == 0


def time_to_search_for_collision(hash_value: str, last_digits: int, bins: List[int]) -> None:
    """
    Measures the time it takes to search for a collision using different numbers of processes.

    Args:
        hash_value (str): The hash value to search for.
        last_digits (int): The last four digits of the card number.
        bins (List[int]): A list of bin numbers.
    """
    time_list = []
    for count_cpu in tqdm(range(1, int(1.5 * mp.cpu_count())), desc="Searching for collision"):
        start = time.time()
        if select_card_number(hash_value, last_digits, bins, count_cpu):
            time_list.append(time.time() - start)

    x = list(range(1, int(1.5 * mp.cpu_count())))
    y = time_list

    plt.figure(figsize=(30, 5))
    plt.xlabel('Number of Processes')
    plt.ylabel('Execution Time, s')
    plt.title('Relationship between Number of Processes and Time')
    plt.plot(x, y, color='m', linestyle='--',
             marker='x', linewidth=1, markersize=4)
    plt.show()
