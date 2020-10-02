#!/usr/bin/python3
import os, sys

args = sys.argv

if len(args) <= 1:
    sys.exit(1)

n = int(args[1])
base = os.getcwd()
input_path = base + '/../data/hightemp.txt'

with open(input_path, 'r', encoding='utf-8') as f:
    for _ in range(n):
        print(f.readline().rstrip('\n'))
