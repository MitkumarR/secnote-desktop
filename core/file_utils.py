from cryptography.fernet import Fernet
import os

def encrypt_file(filepath, key):
     fernet = Fernet(key)
    
     with open(filepath, "rb") as f:
         original = f.read()
    
     encrypted = fernet.encrypt(original)
     filename = os.path.basename(filepath).replace(".txt", ".enc")

def decrypt_file(filepath, key):
    fernet = Fernet(key)
    
    with open(filepath, "rb") as ef:
        encrypted = ef.read()
    
    decrypted = fernet.decrypt(encrypted)
    filename = os.path.basename(filepath).replace(".enc", ".txt")