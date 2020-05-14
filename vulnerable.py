from hashlib import pbkdf2_hmac
import os

password = raw_input()
salt = os.urandom(8)
hash = pbkdf2_hmac('sha1', password, salt, 1024)

