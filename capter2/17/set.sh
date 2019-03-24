#!/bin/bash
cat ../data/hightemp.txt | cut -f 1 | sort | uniq -c
