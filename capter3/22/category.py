#!/usr/bin/python3
# 否定・肯定先読み：http://www-creators.com/archives/2746
import re, os

pattern = '.*Category:(.*?)(?=(]|(\|\*)))'
#pattern = '.*Category:(.*?)((\|\*)|(]]))'
reg = re.compile(pattern)

path = os.getcwd() + '/../data/article.txt'
extracted_list = []
with open(path, 'r') as f:
    for line in f:
        extracted = reg.match(line)
        if extracted is not None:
            extracted_list.append(extracted)

for e in extracted_list:
    print(e.group(1))
