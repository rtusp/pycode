from hashlib import pbkdf2_hmac
import os

password = raw_input()
hash = pbkdf2_hmac('sha1', password, 'static salt', 1024)

