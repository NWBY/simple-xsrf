# simple-xsrf

A simple package to create CSRF/XSRF tokens and protect against CSRF/XSRF attacks.

### Installation
```
pip install simple-xsrf
```

### Usage

To use this package you will need a fernet key also known as a secret key. To create a key:
```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()
```
**Make sure to store this key in a secure place like a database so that you can access it later. You will need it to create your tokens and decrypt them**

Creating a token:
```python
from simple_xsrf.token import create_xsrf

token = create_xsrf(key)
```

Checking if a token is valid:
```python
from simple_xsrf.token import is_valid

is_token_valid = is_valid(key, token_from_request, token_from_storage)
```
You should store your token in a storage layer such as Redis or DynamoDB to be retrived later.
