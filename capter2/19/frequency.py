#!/usr/bin/python3
# lambda: http://atkonn.blogspot.com/2008/02/python-python27-lambda.html
# sorted(): https://qiita.com/shizuma/items/40f1fe4702608db40ac3
#           https://qiita.com/inon3135/items/70b1ed6706579bd48edf
import os

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        prefectures = []
        for line in f:
            prefectures.append(line.split('\t')[0])
    return prefectures

def write(path, lines):
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

if __name__=='__main__':
    base = os.getcwd()
    input_path = base + '/../data/hightemp.txt'
    
    prefectures = read(input_path)

    prfct_rank = {}
    for p in prefectures:
        if p in prfct_rank.keys():
            prfct_rank[p]+=1
        else:
            prfct_rank[p] = 1

    print(sorted(prfct_rank.items(), key=lambda x:-x[1]))
