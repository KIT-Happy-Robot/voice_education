#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy

def temperature(x, y, z):
    return str(x) + '時の' + str(y) + 'は' + str(z)

x = 12
y = '気温'
z = 22.4

print(temperature(x, y, z))