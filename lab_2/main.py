from NIST_tests import frequency_bitwise_test, same_consecutive_bits_test, longest_sequence_test, maximum_sequence_length
from work_with_file import read_json



def main():
    path_to_file_with_sequences = r'sequences.json'
    key1 = "C++"
    key2 = "Java"
    sequence = read_json(path_to_file_with_sequences)
    #print(sequence[key1])
    print(frequency_bitwise_test(sequence[key1]))
    print(same_consecutive_bits_test(sequence[key1]))
    print(longest_sequence_test(sequence[key1]))
    
if __name__ == "__main__":
    main()
else: 
    pass
