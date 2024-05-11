import argparse

from modules.asymmetric import Asymmetric
from modules.symmetric import Symmetric
from modules import work_with_files

def clean_text_files(file_paths: list):
    """
    Clears the text files specified in the file_paths list from data.

    Args:
    file_paths (list): a list of paths to text files that need to be cleared.
    """
    for file_path in file_paths:
        try:
            with open(file_path, 'w') as file:
                file.write('')
            print(f"Файл '{file_path}' успешно очищен.")
        except FileNotFoundError:
            print(f"Ошибка: файл '{file_path}' не найден.")
        except IOError:
            print(f"Ошибка: не удалось открыть файл '{file_path}'.")

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='Запускает режим генерации ключей')
    group.add_argument('-enc', '--encryption', help='Запускает режим шифрования текста')
    group.add_argument('-dec', '--decryption', help='Запускает режим дешифрования текста')
    group.add_argument('-enck', '--encryption_key', help='Запускает шифрование симметричного ключа')
    group.add_argument('-deck', '--decription_key', help='Запускает дешифрование симметричного ключа')
    group.add_argument('-c', '--clear', help='Освобождает файлы с данными, кроме файла с исходным текстом')
    parser.add_argument('settings', type=str, help='Путь к файлу с настройками', default='settings.json')

    args = parser.parse_args()
    
    symmetric = Symmetric()
    asymmetric = Asymmetric()

    settings = work_with_files.read_json(args.settings)
    
    match args:
        case args if args.generation:
            symmetric.key_generation()
            symmetric.serialization_key(settings['symmetric_key'])

            asymmetric.generating_key_pair()
            asymmetric.serialization_private_key(settings['private_key'])
            asymmetric.serialization_public_key(settings['public_key'])

        case args if args.encryption:
            e_text = symmetric.text_encryption(work_with_files.read_txt(settings['initial_file']))
            work_with_files.write_to_txt(e_text, settings['encrypted_file'])

            print(f'Текст зашифрован и направлен в файл {settings['encrypted_file']}')

        case args if args.enck:
            symmetric_key = symmetric.deserialization_key(settings['symmetric_key'])
            asymmetric.encrypt_symmetric_key(symmetric_key)

            asymmetric.serialization_private_key(settings['private_key'])
            asymmetric.serialization_public_key(settings['public_key'])

            print(f'Симметричный ключ зашифрован, приватный ключ направлен в '
                   f'{settings["private_key"]}, публичный в {settings["public_key"]}')
            
        case args if args.deck:
            symmetric_key = asymmetric.decryption_symmetric_key(work_with_files.read_bytes(settings['public_key']))
            
            work_with_files.write_bytes_to_txt(symmetric_key, settings['decrypted_symmetric'])

            print(f'Симметричный ключ расшифрован и направлен в {settings["decrypted_symmetric"]}')

        case args if args.dec:
            dec_symmetric_key = symmetric.deserialization_key(settings['decrypted_symmetric'])
            dec_text = symmetric.decryption_text(dec_symmetric_key)

            work_with_files.write_to_txt(dec_text, settings['decrypted_text'])

            print(f'Текст расшифрован и направлен в {settings["decrypted_text"]}')

        case args if args.clear:
            clean_text_files([settings['decrypted_symmetric'], settings['decrypted_text'],
                              settings['encrypted_file'], settings['private_key'], 
                              settings['public_key'], settings['symmetric_key']])
            print("Все файлы очищены успешно")

        case _:
            print("Выберите режим работы!")

            



    

if __name__ == '__main__':
    main()