import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from modules.work_with_files import *

class Symmetric:
    """
    Class for working with symmetric encryption algorithms.
    """
    def __init__(self):
        self.key = None

    def key_generation(self) -> bytes:
        """
        Generate a random 16 byte encryption key.

        Returns:
        self.key(bytes): encryption key.
        """
        
        self.key = os.urandom(16)
        return self.key
    
    def serialization_key(self, path: str)->None:
        """
        Serializing the symmetric algorithm key to a file.

        Args:
        path(str): path to file for writing.

        Returns:
        None
        """
        write_bytes_to_txt(self.key, path)

    def deserialization_key(self, path: str)->None:
        """
        Deserialization of the symmetric algorithm key.

        Params:
        path(str): path to file whith data

        Returns:
        bytes
        """
        self.key = read_bytes(path)
        return self.key

    def __data_padding(self, text: str):
        """
        Data padding for block cipher operation - we make the message length 
        a multiple of the length of the encrypted block.

        Args: 
        text(str): the message that needs to be padded.

        Returns:
        bytes: a byte message that is a multiple of the length of the encrypted block.
        """
        padder = padding.PKCS7(128).padder()
        btext = bytes(text, 'UTF-8')
        padded_text = padder.update(btext) + padder.finalize()

        return padded_text
    
    def text_encryption(self, text: str, key: bytes)->str:
        """
        Encrypt text using a symmetric algorithm.

        Args:
        text (str): text to be encrypted.

        Returns:
        str: encrypted text.
        """
        iv = os.urandom(16)
        cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(self.__data_padding(text)) + encryptor.finalize()
        c_text = iv + c_text
        return c_text
    
    def __text_depadding(self, dc_text: bytes)->str:
        """
        Remove padding from the decrypted text.

        Args:
        dc_text (bytes): decrypted text with padding.

        Returns:
        str: decrypted text without padding.
        """
        unpadder = padding.PKCS7(128).unpadder()
        unpadder_dc_text = unpadder.update(dc_text) + unpadder.finalize()

        return unpadder_dc_text.decode('UTF-8')
    
    def decryption_text(self, c_text: bytes, key: bytes)->str:
        """
        Decrypt ciphertext using a symmetric algorithm.

        Args:
        c_text (bytes): ciphertext to be decrypted.

        Returns:
        str: decrypted text.
        """
        iv = c_text[:16]
        cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        dc_text = decryptor.update(c_text[16:]) + decryptor.finalize()

        unpadder_dc_text = self.__text_depadding(dc_text)

        return unpadder_dc_text
        
