from hashlib import pbkdf2_hmac
import os

password = raw_input()
pbkdf2_hmac('sha256', password, 'abcd1234', 1024, 128)
