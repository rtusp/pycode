from hashlib import pbkdf2_hmac
import os

password = raw_input()
salt = os.urandom(8)
pbkdf2_hmac('sha256', password, "statyczna sol", 1024, 128)

