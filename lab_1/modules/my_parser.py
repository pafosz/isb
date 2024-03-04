import argparse
import os

from modules.cypher import *
from modules.decypher import *
from modules.text_operations import *


def working_with_terminal():
    parser = argparse.ArgumentParser(description='Text encryption and decryption')

    parser.add_argument('action', choices=['encrypt', 'decrypt'], 
                        default='encrypt', 
                        help='choose an action: encrypt or decrypt')
    
    parser.add_argument('-m', '--method', choices=['Caesar', 'frequency'], 
                        default='Caesar',
                        help='choose the decryption method: Caesar cipher'
                          'or frequency analysis method')
    
    parser.add_argument('-k', '--key', type=str, 
                        default=os.path.join('texts', 'first_part', 'encryption_key.json'),
                        help='the encryption key for Caesar encryption')
    
    parser.add_argument('-inpf', '--input_file',
                        default=os.path.join('texts', 'first_part', 'src_text.txt'),
                        help='the path to the text file')
    
    parser.add_argument('-outf', '--output_file',
                        default=os.path.join('texts', 'first_part', 'decrypted_text.txt'), 
                        help='the path to the file for writing the text')
    
    args = parser.parse_args()

    match args.action:
        
        case 'encrypt':
            
            if not args.key or not args.input_file or not args.output_file:
                print('to encrypt, you must specify the encryption KEY, the path ' 
                     'to the text file, and the path to the output file')
            
            else:
               print('you have chosen to encrypt the text')
               try:
                  source_text = read_text(args.input_file)
                  key = read_json(args.key)['key']
                  cypher = сaesar_cypher(source_text, key)
                  write_file(args.output_file, cypher)
               except Exception as e:
                  print(f'An error occurred while encrypting: {str(e)}')
        
        case 'decrypt':
          match args.method:
             
             case 'Caesar':
                if not args.key or not args.input_file or not args.output_file:
                   print('to decrypt using the reverse Caesar method, '
                         'you must specify the encryption KEY, the path '
                         'to the text file and the path to the output file')
                else:
                   print('you have chosen to decrypt the text using the Caesar method')
                   try:
                      encrypted_text = read_text(args.input_file)
                      key = read_json(args.key)['key']
                      decrypted_text = decypher_caesar(encrypted_text, key)
                      write_file(args.output_file, decrypted_text)
                   except Exception as e:
                      print(f'An error occurred while decrypting: {str(e)}')

             case 'frequency':
                if not args.key or not args.input_file or not args.input_file:
                    print('to decrypt using the frequency analysis method, ' 
                             'you must specify the PATH to the key location, ' 
                             'to the text file and to the output file')
                else:
                   print('you have chosen to decrypt the text using the frequency analysis method')
                   try:
                      encrypted_text = read_text(args.input_file)
                      key = read_json(args.key)
                      decrypted_text = decrypt_by_key(encrypted_text, key)
                      write_file(args.output_file, decrypted_text)
                   except Exception as e:
                      print(f'An error occurred while decrypting: {str(e)}')

             case _:
                print('you did not specify the decryption method')
                
        case _:
          print('you did not specify the action or the action does not exist')
          
                   