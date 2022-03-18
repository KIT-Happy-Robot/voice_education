#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy

def ngram(S, n):
    r = []
    for i in range(len(S) - n + 1):
        r.append(S[i:i + n])
    return r

s1 = 'paraparaparadise'
s2 = 'paragraph'

st1 = set(ngram(s1, 2))
st2 = set(ngram(s2, 2))

print(st1 | st2)
print(st1 & st2)
print(st1 - st2)

print('se' in st1)
print('se' in st2)
