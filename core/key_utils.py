from cryptography.fernet import Fernet
import os

DIR = "secret_keys/"
KEY_PATH = f"{DIR}secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as f:
        f.write(key)
    return key

def load_key():
    if not os.path.exists(KEY_PATH):
        raise FileNotFoundError("Key file not found.")
    with open(KEY_PATH, "rb") as f:
        return f.read()
