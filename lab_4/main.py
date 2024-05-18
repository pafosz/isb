import multiprocessing as mp

from modules import work_with_files, number_card


if __name__ == "__main__":
    hash = work_with_files.read_json('card_information.json')['hash']
    last_digits = work_with_files.read_json('card_information.json')['last_digits']
    bins = work_with_files.read_json('card_information.json')['bins']
    # mp.freeze_support()
    # number_card.time_to_search_for_collision(hash, last_digits, bins)
    print(work_with_files.read_json('card_number.json'))
    print(number_card.algorithm_Luna(work_with_files.read_json('card_number.json')))
    print(work_with_files.read_txt('bins.txt'))