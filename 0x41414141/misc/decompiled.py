import base64
import binascii

secret = 'https://google.com'
cipher2 = [b'NDE=', b'NTM=', b'NTM=', b'NDk=', b'NTA=', b'MTIz', b'MTEw', b'MTEw', b'MzI=', b'NTE=', b'MzQ=', b'NDE=',
           b'NDA=', b'NTU=', b'MzY=', b'MTEx', b'NDA=', b'NTA=', b'MTEw', b'NDY=', b'MTI=', b'NDU=', b'MTE2', b'MTIw']
cipher1 = [base64.b64encode(str(ord(i) ^ 65).encode()) for i in secret]

decoded2 = [chr(int(base64.b64decode(i)) ^ 65) for i in cipher2]
print(''.join(decoded2))

f = open("decoded", "r")
line = []
for x in f:
    splitted = x.split("\\x")
    for i in splitted:
        if len(i) == 2:
            line.append(i)
print(" ".join(line))