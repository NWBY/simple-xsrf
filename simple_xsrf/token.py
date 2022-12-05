from cryptography.fernet import Fernet, InvalidToken
from .exceptions import InvalidXsrfToken
import string
import random

def create_xsrf(key: str) -> str:
    ft = Fernet(key)
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
    byte_string = random_string.encode('utf-8') 
    token = ft.encrypt(byte_string)
    
    return token.decode('utf-8')

def decrypt_token(key: str, token: str) -> str:
    ft = Fernet(key)

    try:
        decrypted_token = ft.decrypt(token)
    except InvalidToken:
        raise InvalidXsrfToken('Token is not valid')

    return decrypted_token.decode('utf-8')

def is_valid(key: str, token: str, stored_token: str) -> bool:
    ft = Fernet(key)    

    try:
        decrypted_token = ft.decrypt(token)
        decrypted_stored_token = ft.decrypt(stored_token)
    except InvalidToken:
        raise InvalidXsrfToken('Token is not valid')

    return decrypted_token == decrypted_stored_token
