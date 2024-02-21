from modules.text_operations import *
from modules.cypher import *
from modules.decypher import *

KEY = 3
PATH_FOR_READ = f'texts\\first_part'
PATH_FOR_WRITE_ENCRYPTED = f'texts\\first_part\encrypted_text.txt'
PATH_FOR_WRITE_DECRYPTED = f'texts\\first_part\decrypted_text.txt'

# ОСТАВИТЬ!!!
#write_file(PATH_FOR_WRITE_ENCRYPTED, сaesar_cypher(read_text(PATH_FOR_READ, 'src_text.txt'), KEY))
#write_file(PATH_FOR_WRITE_DECRYPTED, decypher_caesar(read_text(PATH_FOR_READ, 'encrypted_text.txt'), KEY))
#write_to_json(f'texts\\first_part\encryption_key.json', key)
# ОСТАВИТЬ!!!

# print(detect(read_text(f'texts\\first_part', 'src_text.txt')))
# print(detect(read_text(f'texts\\first_part', 'encrypted_text.txt')))
# print(read_text(f'texts\\first_part', 'src_text.txt'))
# write_file('texts\\first_part\src_text1.txt', 'hi')

#сaesar_cypher(read_text('texts\\first_part', 'src_text.txt'), 2)

key = {'key': 3}
#
print(read_json(f'texts\\first_part\encryption_key.json').values())