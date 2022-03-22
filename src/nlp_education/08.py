#!/usr/bin/env python
#-*- coding: utf-8 -*-

def cipher(S):
    new = []
    for s in S:
        if 97 <= ord(s) <= 122:
            s = chr(219 - ord(s))
        new.append(s)
    return ''.join(new)

s = 'I am an NLPer'
new = cipher(s)
print(new)

print(cipher(new))
