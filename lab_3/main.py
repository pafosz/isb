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


def actions_for_generating_keys(symmetric: Symmetric, asymmetric: Asymmetric, settings: dict)->None:
    symmetric.key_generation()
    symmetric.serialization_key(settings['symmetric_key'])

    asymmetric.generating_key_pair()
    asymmetric.serialization_private_key(settings['private_key'])
    asymmetric.serialization_public_key(settings['public_key'])

    print(f'Ключи сгенерированы и сериализованы в {settings["symmetric_key"], \
                                                    settings["private_key"], \
                                                    settings["public_key"]}')
    
    
def actions_for_encrypting_text(symmetric: Symmetric, settings: dict)->None:
    symmetric_key = symmetric.deserialization_key(settings['symmetric_key'])
    text = work_with_files.read_txt(settings['initial_file'])
    e_text = symmetric.text_encryption(text, symmetric_key)
    work_with_files.write_bytes_to_txt(e_text, settings['encrypted_file'])

    print(f'Текст зашифрован и направлен в файл {settings['encrypted_file']}')


def actions_to_encrypt_symmetric_key(symmetric: Symmetric, asymmetric: Asymmetric, settings: dict)->None:
    symmetric_key = symmetric.deserialization_key(settings['symmetric_key'])
    work_with_files.write_bytes_to_txt(asymmetric.encrypt_symmetric_key(symmetric_key, settings['public_key']), 
                                               settings['encrypted_symmetric'])            

    print(f'Симметричный ключ зашифрован и направлен в {settings['encrypted_symmetric']}')


def actions_to_decrypt_symmetric_key(asymmetric: Asymmetric, settings: dict)->None:
    esymmetric_key = work_with_files.read_bytes(settings['encrypted_symmetric'])
    symmetric_key = asymmetric.decryption_symmetric_key(esymmetric_key, settings['private_key'])            
    work_with_files.write_bytes_to_txt(symmetric_key, settings['decrypted_symmetric'])

    print(f'Симметричный ключ расшифрован и направлен в {settings["decrypted_symmetric"]}')


def actions_for_decrypting_text(symmetric: Symmetric, settings: dict)->None:
    dec_symmetric_key = symmetric.deserialization_key(settings['decrypted_symmetric'])
    text = work_with_files.read_bytes(settings['encrypted_file'])
    dec_text = symmetric.decryption_text(text, dec_symmetric_key)
    work_with_files.write_to_txt(dec_text, settings['decrypted_text'])

    print(f'Текст расшифрован и направлен в {settings["decrypted_text"]}')


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-gen', '--generation', help='Запускает режим генерации ключей', action='store_true')
    group.add_argument('-enc', '--encryption', help='Запускает режим шифрования текста', action='store_true')
    group.add_argument('-dec', '--decryption', help='Запускает режим дешифрования текста', action='store_true')
    group.add_argument('-enck', '--encryption_key', help='Запускает шифрование симметричного ключа', action='store_true')
    group.add_argument('-deck', '--decription_key', help='Запускает дешифрование симметричного ключа', action='store_true')
    group.add_argument('-c', '--clear', help='Освобождает файлы с данными, кроме файла с исходным текстом', action='store_true')
    parser.add_argument('settings', type=str, help='Путь к файлу с настройками', default='settings.json')

    args = parser.parse_args()
    
    symmetric = Symmetric()
    asymmetric = Asymmetric()

    settings = work_with_files.read_json('settings.json')
    
    match args:
        case args if args.generation:
            actions_for_generating_keys(symmetric, asymmetric, settings)

        case args if args.encryption:
           actions_for_encrypting_text(symmetric, settings)

        case args if args.encryption_key:
            actions_to_encrypt_symmetric_key(symmetric, asymmetric, settings)
            
        case args if args.decription_key:
            actions_to_decrypt_symmetric_key(asymmetric, settings)

        case args if args.decryption:
            actions_for_decrypting_text(symmetric, settings)

        case args if args.clear:
            clean_text_files([settings['decrypted_symmetric'], settings['decrypted_text'],
                              settings['encrypted_file'], settings['private_key'], 
                              settings['public_key'], settings['symmetric_key']])
            print("Все файлы очищены успешно")

        case _:
            print("Выберите режим работы!")
    

if __name__ == '__main__':
    main()
    