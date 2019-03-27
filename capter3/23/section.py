#!/usr/bin/python3
# wikiセクション：https://ja.wikipedia.org/wiki/Help:%E3%82%BB%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3
import os, re

def disp(level, level_list):
    print('--level {}--'.format(level))
    for e in level_list:
        print(e.group(1))
    print()

level1 = '^={2}([^=].+)={2}'
level2 = '^={3}([^=].+)={3}'
level3 = '^={4}([^=].+)={4}'
reg1 = re.compile(level1)
reg2 = re.compile(level2)
reg3 = re.compile(level3)

path = os.getcwd() + '/../data/article.txt'

level1_list = []
level2_list = []
level3_list = []
with open(path, 'r') as f:
    for line in f:
        extracted1 = reg1.match(line)
        if extracted1 is not None:
            level1_list.append(extracted1)
            continue
        
        extracted2 = reg2.match(line)
        if extracted2 is not None:
            level2_list.append(extracted2)
            continue

        extracted3 = reg3.match(line)
        if extracted3 is not None:
            level3_list.append(extracted3)

ll = [1, 2, 3]
lll = [level1_list, level2_list, level3_list]
for level, level_list in zip(ll, lll):
    disp(level, level_list)

