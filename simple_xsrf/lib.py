from cryptography.fernet import Fernet
from os import environ
import string
import random

def get_key() -> str | None:
    return environ.get('ENCRYPTION_KEY')

def create_xsrf(key: str) -> str:
    ft = Fernet(key)
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
    byte_string = random_string.encode('utf-8') 
    token = ft.encrypt(byte_string)
    
    return token.decode('utf-8')

def decrypt_token(key: str, token: str) -> str:
    ft = Fernet(key)
    decrypted_token = ft.decrypt(token)

    return decrypted_token.decode('utf-8')

def is_valid(key: str, token: str, stored_token: str) -> bool:
    ft = Fernet(key)    

    decrypted_token = ft.decrypt(token)
    decrypted_stored_token = ft.decrypt(stored_token)

    return decrypted_token == decrypted_stored_token
