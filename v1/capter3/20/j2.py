#!/usr/bin/python3
import json, os

base = os.getcwd()
input_path = base + '/../data/england.json'

with open(input_path, 'r') as f:
    jdata = json.load(f)

output_path = base + '/../data/article.txt'
with open(output_path, 'w') as f:
    f.write(jdata['text'])  # イギリスの記事本文
