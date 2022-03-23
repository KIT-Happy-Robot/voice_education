#!/usr/bin/env python
#-*- coding: utf-8 -*-

s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s = s.replace(',', '').replace('.', '')

t = [len(w) for w in s.split()]
print(t)
