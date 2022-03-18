#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy

path = 'neko.txt.mecab'
with open(path) as f:
    text = f.read().split('\n')
result = []
for line in text:
    if line == 'EOS':
        continue
    #elif line == '':
    #    continue
    ls = line.split('\t')
    d = {}
    tmp = ls[1].split(',')
    d = {'surface':ls[0], 'base':tmp[6], 'pos':tmp[0], 'posl':tmp[1]}
    result.append(d)
print(result)
