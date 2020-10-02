#!/usr/bin/python3
import os, re

pattern = '(File:(.+?)\||ファイル:(.+?)\|)' 
reg = re.compile(pattern)
media_list = []

path = os.getcwd() + '/../data/article.txt'
with open(path, 'r') as f:
    for line in f:
        media = reg.match(line)
        if media is not None:
            media_list.append(media)

print(len(media_list))
for m in media_list:
    print(m)
