# coding:utf-8
import argparse

def decrypt(target):
    print('DECRIPT')
    print(target)
    

# https://www.k-cube.co.jp/wakaba/server/ascii_code.html
def encrypt(target):
    print('ECRIPT')
    print(target)

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
