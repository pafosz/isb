from NIST_tests import *
from work_with_file import read_json

def main():
    path_to_file_with_sequences = r'sequences.json'
    key1 = "C++"
    key2 = "Java"
    sequence = read_json(path_to_file_with_sequences)

    print(f"Частотный побитовый тест (C++): {frequency_bitwise_test(sequence[key1])}\n")
    print(f"Тест на одинаковые подряд идущие биты (C++): {same_consecutive_bits_test(sequence[key1])}\n")
    print(f"Тест на самую длинную последовательность единиц в блоке (C++): {longest_sequence_test(sequence[key1])}\n\n")

    print(f"Частотный побитовый тест (Java): {frequency_bitwise_test(sequence[key2])}\n")
    print(f"Тест на одинаковые подряд идущие биты (Java): {same_consecutive_bits_test(sequence[key2])}\n")
    print(f"Тест на самую длинную последовательность единиц в блоке (Java): {longest_sequence_test(sequence[key2])}\n")
    
if __name__ == "__main__":
    main()
else: 
    pass
