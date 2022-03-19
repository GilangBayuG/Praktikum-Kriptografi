Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import long_to_bytes

data = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
bytes = long_to_bytes(data)
print(bytes)