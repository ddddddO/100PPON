import argparse

def decrypt(target):
    print(target)
    print('DECRIPT')

def encrypt(target):
    print(target)
    print('ENCRYPT')

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
