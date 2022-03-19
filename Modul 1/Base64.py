Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from base64 import *
flag = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
flag = bytes.fromhex(flag)
print(b64encode(flag))
b'crypto/Base+64+Encoding+is+Web+Safe/'
