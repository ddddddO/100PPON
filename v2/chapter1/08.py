def cipher(s):
    rslt = ''
    for c in s:
        code = ord(c)
        if code in range(97, 123):
            rslt += chr(219-code)
        else:
            rslt += c
    return rslt

src = 'adeArf0@>c'
print('src: {src}'.format(src = src))

print('-' * 30)

encrypted = cipher(src)
print(encrypted)

print('-' * 30)

decrypted = cipher(encrypted)
print(decrypted)