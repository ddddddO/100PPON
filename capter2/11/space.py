#!/usr/bin/python3
import os

input_path = os.getcwd() + '/../data/hightemp.txt'
with open(input_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

space_lines = []
for line in lines:
    space_lines.append(line.replace('\t', ' ').rstrip('\n'))

for sline in space_lines:
    print(sline)
