#!/usr/bin/python3
# 正規表現参考：https://qiita.com/luohao0404/items/7135b2b96f9b0b196bf3

import re, os

pattern = '.*Category.*'
reg = re.compile(pattern)

path = os.getcwd() + '/../data/article.txt'
extracted_list = []
with open(path, 'r') as f:
    for line in f:
        extracted = reg.match(line)
        if extracted is not None:
            extracted_list.append(extracted)

for e in extracted_list:
    print(e.group())
