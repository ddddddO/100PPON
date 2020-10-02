#!/usr/bin/python3
import os, sys

base = os.getcwd()
input_path = base + '/../data/hightemp.txt'

with open(input_path, 'r', encoding='utf-8') as f:
    prefectures = []
    for line in f:
        prefectures.append(line.split('\t')[0])

print(set(prefectures))