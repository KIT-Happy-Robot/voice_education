#!/usr/bin/env python
#-*- coding: utf-8 -*-

def ngram(S, n):
    r = []
    for i in range(len(S) - n + 1):
        r.append(S[i:i+n])
    return r

s = 'I am an NLPer'

print (ngram(s.split(),2))
print (ngram(s,2))
