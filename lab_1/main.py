import argparse

from modules.cypher import *
from modules.encryption_function import *
from modules.text_operations import *

def main():
    parser = argparse.ArgumentParser(description='Text encryption and decryption')

    parser.add_argument('action', choices=[Mode.ENCRYPT.value, Mode.DECRYPT.value], 
                        help='choose an action: encrypt or decrypt')
    
    parser.add_argument('-m', '--method', choices=[Method.CAESAR.value, Method.FREQUENCY.value], 
                        help='choose the decryption method: Caesar cipher,'
                          'or frequency analysis method')
    
    parser.add_argument('-k', '--key', type=str, 
                        help='the encryption key for Caesar encryption')
    
    parser.add_argument('-inpf', '--input_file',
                        help='the path to the text file')
    
    parser.add_argument('-outf', '--output_file',
                        help='the path to the file for writing the text')
    
    args = parser.parse_args()

    encryption(args.action, args.method, args.key, args.input_file, args.output_file)
    
if __name__ == '__main__':    
    main()
else: 
    print('Error')
