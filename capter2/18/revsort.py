#!/usr/bin/python3
import os

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def write(path, lines):
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def bubble_rev(lines):
    length = len(lines) - 1
    for i in range(length):
        for j in range(length, i, -1):
            if lines[j-1].split('\t')[2] > lines[j].split('\t')[2]:
                lines[j-1], lines[j] = lines[j], lines[j-1]
    return lines

if __name__=='__main__':
    base = os.getcwd()
    input_path = base + '/../data/hightemp.txt'
    output_path = base + '/../data/18/sorted_temp.txt'
    
    lines = bubble_rev(read(input_path))
    write(output_path, lines)
