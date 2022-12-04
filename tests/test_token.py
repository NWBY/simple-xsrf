from simple_xsrf.token import get_key, create_xsrf, decrypt_token, is_valid
from cryptography.fernet import Fernet

def test_get_key_returns_none_is_env_is_not_set():
    assert get_key() == None

def test_create_xsrf():
    key = Fernet.generate_key()

    token = create_xsrf(key)

    assert token is not None and type(token) == str

def test_decrypt_token():
    key = Fernet.generate_key()

    token = create_xsrf(key)
    decrypted_token = decrypt_token(key, token)

    assert decrypted_token is not None and type(decrypted_token) == str

def test_is_valid_with_equal_tokens():
    key = Fernet.generate_key()

    token = create_xsrf(key)
    stored_token = token

    is_token_valid = is_valid(key, token, stored_token)

    assert is_token_valid == True

def test_is_valid_with_inequal_tokens():
    key = Fernet.generate_key()

    token = create_xsrf(key)
    new_token = create_xsrf(key)

    is_token_valid = is_valid(key, token, new_token)

    assert is_token_valid == False
