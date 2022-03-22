#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os.path

file_path = os.path.expanduser('~/catkin_ws/src/nlp100/neko.txt.mecab')
with open(file_path) as f:
    text = f.read().split('\n')
result = []
for line in text:
    if line == 'EOS':
        continue
    elif line == '':
        continue
    ls = line.split('\t')
    d = {}
    tmp = ls[1].split(',')
    d = {'surface':ls[0], 'base':tmp[6], 'pos':tmp[0], 'posl':tmp[1]}
    result.append(d)
print(result)
