from modules.cypher import *
from modules.decypher import *
from modules.text_operations import *

class Method(Enum):
   CAESAR = 'caesar'
   FREQUENCY = 'frequency'

class Default(Enum):
   KEY = r'texts\first_part\encryption_key.json'
   SOURCE_TEXT = r'texts\first_part\src_text.txt'
   OUTPUT_FILE = r'texts\first_part\encrypted_text.txt'

def encryption(mode: Mode = Mode.ENCRYPT.value, 
               method: Method = None, 
               path_to_key: str = Default.KEY.value, 
               path_to_source_text: str=Default.SOURCE_TEXT.value, 
               path_to_output_file: str=Default.OUTPUT_FILE.value) -> None:
    '''
    The function does all the work with encryption in the aggregate.
            Parameters:    
                    mode (Mode): function operation mode ('encrypt' - encrypt text, 'decrypt' - decrypt text)
                    method (Method): decryption method ('caesar' - Caesar cipher, 
                    'frequency' - frequency analysis method), if you need to encrypt, the default parameter is None
                     path_to_key (str): the path to the encryption key
                     path_to_source_text (str): the path to the source text
                     path_to_output_file (str): the path to the output file
            Return value:
                    None
    '''
    match mode:      
         
        case Mode.ENCRYPT.value:            
            if not path_to_key or not path_to_source_text or not path_to_output_file:
                print('to encrypt, you must specify the encryption KEY, the path ' 
                     'to the text file, and the path to the output file')
            
            else:
               print('you have chosen to encrypt the text')
               try:
                  source_text = read_text(path_to_source_text)
                  key = read_json(path_to_key)['key']
                  cypher = сaesar_cypher(source_text, key, 0)
                  write_file(path_to_output_file, cypher)
               except Exception as e:
                  print(f'An error occurred while encrypting: {str(e)}')
        
        case Mode.DECRYPT.value:          
          match method:
             
             case Method.CAESAR.value:
                if not path_to_key or not path_to_source_text or not path_to_output_file:
                   print('to decrypt using the reverse Caesar method, '
                         'you must specify the encryption KEY, the path '
                         'to the text file and the path to the output file')
                else:
                   print('you have chosen to decrypt the text using the Caesar method')
                   try:
                      encrypted_text = read_text(path_to_source_text)
                      key = read_json(path_to_key)['key']
                      decrypted_text = сaesar_cypher(encrypted_text, key, 1)
                      write_file(path_to_output_file, decrypted_text)
                   except Exception as e:
                      print(f'An error occurred while decrypting: {str(e)}')

             case Method.FREQUENCY.value:
                if not path_to_key or not path_to_source_text or not path_to_output_file:
                    print('to decrypt using the frequency analysis method, ' 
                             'you must specify the PATH to the key location, ' 
                             'to the text file and to the output file')
                else:
                   print('you have chosen to decrypt the text using the frequency analysis method')
                   try:
                      encrypted_text = read_text(path_to_source_text)
                      key = read_json(path_to_key)
                      decrypted_text = decrypt_by_key(encrypted_text, key)
                      write_file(path_to_output_file, decrypted_text)
                   except Exception as e:
                      print(f'An error occurred while decrypting: {str(e)}')

             case _:
                print('you did not specify the decryption method')
                
        case _:
          print('you did not specify the action or the action does not exist')
