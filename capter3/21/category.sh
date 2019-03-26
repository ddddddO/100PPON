#!/bin/bash
path=../data/article.txt

cat $path | grep -E '.*Category.*'
