#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy

s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

s = s.replace('.', '')
idx = [1, 5, 6, 7, 8, 9, 15, 16, 19]
mp = {}

for i, w in enumerate(s.split()):
    if (i + 1) in idx:
        v = w[:1]
    else:
        v = w[:2]
    mp[v] = i + 1

print(mp)
