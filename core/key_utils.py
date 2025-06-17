import base64

from cryptography.fernet import Fernet

def is_valid_fernet_key(key_str):
    try:
        # Must decode successfully from base64 and result in 32 bytes
        key_bytes = base64.urlsafe_b64decode(key_str)
        return len(key_bytes) == 32
    except Exception:
        return False


def generate_key():
    key = Fernet.generate_key()
    return key

