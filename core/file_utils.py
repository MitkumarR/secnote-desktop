from cryptography.fernet import Fernet
import os
import subprocess
import platform

def lock_file(filepath):
    system = platform.system()

    script_dir = os.path.dirname(os.path.abspath(__file__))  # current file directory
    bat_path = os.path.join(script_dir, "lock_file.bat")
    sh_path = os.path.join(script_dir, "lock_file.sh")

    if system == "Windows":
        subprocess.run([bat_path, filepath], shell=True)
    elif system in ["Linux", "Darwin"]:
        subprocess.run(["bash", sh_path, filepath])
    else:
        raise OSError("Unsupported OS")

def encrypt_file(filepath, key):
    fernet = Fernet(key)

    # Step 1: Read original content
    with open(filepath, "rb") as f:
        original = f.read()

    # Step 2: Encrypt it
    encrypted = fernet.encrypt(original)

    # Step 3: Overwrite the file
    with open(filepath, "wb") as f:
        f.write(encrypted)

    # Step 4: Rename the file from .txt to .enc
    if filepath.endswith(".txt"):
        new_path = filepath.replace(".txt", ".enc")
        os.rename(filepath, new_path)

        return new_path  # Return updated path
    else:
        return filepath  # Already encrypted maybe

def decrypt_file(filepath, key):
    fernet = Fernet(key)

    # Step 1: Read encrypted content
    with open(filepath, "rb") as ef:
        encrypted = ef.read()

    # Step 2: Decrypt it
    decrypted = fernet.decrypt(encrypted)

    # Step 3: Overwrite the file
    with open(filepath, "wb") as f:
        f.write(decrypted)

    # Step 4: Rename the file from .enc to .txt
    if filepath.endswith(".enc"):
        new_path = filepath.replace(".enc", ".txt")
        os.rename(filepath, new_path)

        return new_path  # Return updated path
    else:
        return filepath  # Already encrypted maybe
