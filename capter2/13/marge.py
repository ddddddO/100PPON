#!/usr/bin/python3
import os

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = []
        for line in f:
            lines.append(line.rstrip('\n'))

    return lines

if __name__=='__main__':
    base = os.getcwd()
    input_path_1 = base + '/../data/col1.txt'
    input_path_2 = base + '/../data/col2.txt'
    output_path_1 = base + '/../data/marge.txt'
    
    lines1 = read(input_path_1)
    lines2 = read(input_path_2)

    with open(output_path_1, 'w', encoding='utf-8') as f:
        for i in range(len(lines1)):
            if i != len(lines1):
                f.write(lines1[i] + '\t' + lines2[i] + '\n')
            else:
                f.write(lines1[i] + '\t' + lines2[i])
