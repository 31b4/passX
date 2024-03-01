import numpy as np
from login import KEY

def encrypt(raw):
    password_bytes = np.frombuffer(raw.encode(), dtype=np.uint8)
    key_bytes = np.frombuffer(KEY.encode(), dtype=np.uint8)

    repeated_key = np.resize(key_bytes, len(password_bytes))


    encrypted_bytes = password_bytes ^ repeated_key
    encrypted_password = encrypted_bytes.tobytes()

    return encrypted_password

def decrypt(encrypted):
    encrypted_bytes = np.frombuffer(encrypted, dtype=np.uint8)
    key_bytes = np.frombuffer(KEY.encode(), dtype=np.uint8)

    repeated_key = np.resize(key_bytes, len(encrypted_bytes))

    decrypted_bytes = encrypted_bytes ^ repeated_key
    decrypted_password = decrypted_bytes.tobytes().decode()

    return decrypted_password
