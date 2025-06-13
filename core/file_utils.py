from cryptography.fernet import Fernet
import os

class file_utils():

    @classmethod
    def __encrypt_file(cls, filepath, key):
        fernet = Fernet(key)

        with open(filepath, "rb") as f:
            original = f.read()

        encrypted = fernet.encrypt(original)

        filename = os.path.basename(filepath)


    @classmethod
    def __decrypt_file(cls, filepath, key):
        fernet = Fernet(key)
        with open(filepath, "rb") as ef:
            encrypted = ef.read()
        decrypted = fernet.decrypt(encrypted)

        filename = os.path.basename(filepath).replace(".enc", ".dec")



