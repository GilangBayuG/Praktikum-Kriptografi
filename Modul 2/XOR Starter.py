Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
data = "label"
flag = ''

for c in data:
    flag += chr(ord(c) ^ 13)

print('crypto{{{}}}'.format(flag))