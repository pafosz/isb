from modules.text_operations import *
from modules.cypher import *
from modules.decypher import *
import argparse

KEY_1 = 3
PATH_TO_SOURCE_FILE_1 = 'texts\first_part\src_text.txt'
PATH_TO_OUTPUT_FILE_1 = 'out_put.txt'

def main():    

    parser = argparse.ArgumentParser(description='Text encryption and decryption')

    parser.add_argument('action', choices=['encrypt', 'decrypt'], 
                        help='choose an action: encrypt or decrypt')
    
    parser.add_argument('-m', '--method', choices=['Caesar', 'frequency'], 
                        help='choose the decryption method: Caesar cipher'
                          'or frequency analysis method')
    
    parser.add_argument('-k', '--key', 
                        help='the encryption key for Caesar encryption')
    
    parser.add_argument('-inpf', '--input_file',
                         help='the path to the text file')
    
    parser.add_argument('-outf', '--output_file', 
                        help='the path to the file for writing the text')
    
    args = parser.parse_args()

    if args.action == 'encrypt':
        if not args.key or not args.input_file or not args.output_file:
            print('to encrypt, you must specify the encryption KEY, the path ' 
                  'to the text file, and the path to the output file')
        else:
            # try - except
            print('you have chosen to encrypt the text')
            source_text = read_text(args.input_file)
            cypher = сaesar_cypher(source_text, args.key)
            write_file(args.output_file, cypher)

    elif args.action == 'decrypt':
        if args.method == 'Caesar':
                 if not args.key or not args.input_file or not args.output_file:
                      print('to decrypt using the reverse Caesar method, ' 
                            'you must specify the encryption KEY, the path ' 
                            'to the text file and the path to the output file')
                 else:
                    # try - except
                    print('you have chosen to decrypt the text using the Caesar method')
                    encrypted_text = read_text(args.input_file)
                    decrypted_text = decypher_caesar(encrypted_text, args.key)
                    write_file(args.output_file, decrypted_text)
        elif args.method == 'frequency':
             if not args.key or not args.input_file or not args.input_file:
                  print('to decrypt using the frequency analysis method, ' 
                        'you must specify the PATH to the key location, ' 
                        'to the text file and to the output file')
             else:
                  # try - except
                  print('you have chosen to decrypt the text using the frequency analysis method')
                  encrypted_text = read_text(args.input_file)
                  key = read_json(args.key)
                  decrypted_text = decrypt_by_key(encrypted_text, key)
                  write_file(args.output_file, decrypted_text)  
        else:
             print('you did not specify the decryption method')

# зашифровать текст шифром Цезаря              
# python main.py encrypt -k 3 -inpf 'texts\first_part\src_text.txt' -outf 'texts\first_part\encrypted_text.txt'

# расшифровать текст методом Цезаря
#             

if __name__ == '__main__':
    
    main()
else: 
    print('Error')











# ОСТАВИТЬ!!!

# 
# PATH_FOR_READ = f'texts\\first_part'
# PATH_FOR_WRITE_ENCRYPTED = f'texts\\first_part\encrypted_text.txt'
# PATH_FOR_WRITE_DECRYPTED = f'texts\\first_part\decrypted_text.txt'
# PATH_AT_COD5 = r'texts\second_part\cod5.txt'
# PATH_AT_KEY = r'texts\second_part\encryption_key.json'
# write_file(PATH_FOR_WRITE_ENCRYPTED, сaesar_cypher(read_text(PATH_FOR_READ, 'src_text.txt'), KEY))
# write_file(PATH_FOR_WRITE_DECRYPTED, decypher_caesar(read_text(PATH_FOR_READ, 'encrypted_text.txt'), KEY))
# write_to_json(f'texts\\first_part\encryption_key.json', key)
# write_dict_to_json(f'texts\\second_part\\encryption_key.json', 
#                     get_key(read_json('texts\second_part\standard_frequency.json'), read_json('texts\second_part\\frequency_analysis.json')))
# write_dict_to_json(f'texts\\second_part\\frequency_analysis.json', frequency_analysis(read_text(f'texts\\second_part', 'cod5.txt')))
# cypher = read_text(PATH_AT_COD5)
# key = read_json(PATH_AT_KEY)
# dec_txt = decrypt_by_key(cypher, key)
# write_file(r'texts\second_part\decrypted_text.txt', dec_txt)

# ОСТАВИТЬ!!!

