#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy

s1 = 'パトカー'
s2 = 'タクシー'

print(''.join([a + b for a, b in zip(s1, s2)]))
