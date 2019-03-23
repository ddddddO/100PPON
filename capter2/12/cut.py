#!/usr/bin/python3
import os

def read(path):
    with open(input_path, 'r', encoding='utf-8') as f:
        col1, col2 = [], []
        for line in f:
            tmp = line.split('\t')
            col1.append(tmp[0])
            col2.append(tmp[1])

    return col1, col2

def write(col1, col2, path1, path2):
    with open(path1, 'w', encoding='utf-8') as f:
        f.write('\n'.join(col1))

    with open(path2, 'w', encoding='utf-8') as f:
        f.write('\n'.join(col2))

# https://note.nkmk.me/python-file-io-open-with/
if __name__=='__main__':
    base = os.getcwd()
    input_path = base + '/../data/hightemp.txt'
    output_path_1 = base + '/../data/col1.txt'
    output_path_2 = base + '/../data/col2.txt'

    col1, col2 = read(input_path)
    write(col1, col2, output_path_1, output_path_2)
