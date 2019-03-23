#!/usr/bin/python3
import os

os.chdir('../data')
input_path = os.getcwd() + '/hightemp.txt'

with open(input_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(len(lines))
