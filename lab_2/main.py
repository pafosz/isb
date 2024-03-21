from NIST_tests import frequency_bitwise_test
from work_with_file import read_json



def main():
    path_to_file_with_sequences = r'sequences.json'
    key1 = "C++"
    key2 = "Java"
    sequence = read_json(path_to_file_with_sequences)
    #print(sequence[key1])
    print(frequency_bitwise_test(sequence[key2]))
    
if __name__ == "__main__":
    main()
else: 
    pass