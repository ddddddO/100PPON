#!/usr/bin/python3
import os, sys

args = sys.argv

if len(args) <= 1:
    sys.exit(1)

n = int(args[1])
base = os.getcwd()
input_path = base + '/../data/hightemp.txt'
length = sum(1 for line in open(input_path))

with open(input_path, 'r', encoding='utf-8') as f:
    c = 0
    offset = length - n

    for line in f:
        if c >= offset:
            print(line.rstrip('\n'))            
        c+=1
