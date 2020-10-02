#!/usr/bin/python3
import os, sys

# リスト分割: https://www.python.ambitious-engineer.com/archives/1843
# yield: https://www.sejuku.net/blog/23716

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def split(lines, split_n):
    for i in range(0, len(lines), split_n):
        yield lines[i:i+split_n]

def write(base, ll):
    output_path = base + '/../data/16/py/splited'
    suffix = 0
    for lines in ll:
        with open(output_path+str(suffix), 'w', encoding='utf-8') as f:
            f.writelines(lines)
        suffix += 1

if __name__=='__main__':
    args = sys.argv
    if len(args) != 2:
        sys.exit(1)

    n = int(args[1])
    base = os.getcwd()
    input_path = base + '/../data/hightemp.txt'

    lines = read(input_path)
    ll = list(split(lines, n))
    write(base, ll)