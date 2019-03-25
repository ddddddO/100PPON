#!/usr/bin/python3
import json, os

base = os.getcwd()
json_path = base + '/../data/jawiki-country.json'

with open(json_path, 'r') as f:
    england = ''
    for line in f:
        if 'title": "イギリス' in line:
            england = line

with open(base + '/../data/england.json', 'w') as f:
    f.write(england)