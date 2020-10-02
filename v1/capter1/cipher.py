# coding:utf-8
import argparse

def decrypt(target):
    print('DECRYPT')

    decrypted_text = ''
    for char in target:
        n = 219 - ord(char)
        if 97 <= n and n <= 122:
            decrypted_text += chr(n)
        else:
            decrypted_text += char

    print(decrypted_text)

# https://www.k-cube.co.jp/wakaba/server/ascii_code.html
def encrypt(target):
    print('ENCRYPT')

    encrypted_text = ''
    for char in target:
        n = ord(char)
        if 97 <= n and n <= 122:
            encrypted_text += chr(219-n)
        else:
            encrypted_text += char
    
    print(encrypted_text)

# cipher.py encrypt/decrypt -t <str>
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='encryption and decryption')
    subparsers = parser.add_subparsers()

    # encrypt
    parser_encrypt = subparsers.add_parser('encrypt')
    parser_encrypt.add_argument('-t', '--target', type=str, help='encrypt!')
    parser_encrypt.set_defaults(handler=encrypt)

    # decrypt
    parser_decrypt = subparsers.add_parser('decrypt')
    parser_decrypt.add_argument('-t', '--target', type=str, help='decrypt!')
    parser_decrypt.set_defaults(handler=decrypt)    

    args = parser.parse_args()

    if hasattr(args, 'handler'):
        args.handler(args.target)
