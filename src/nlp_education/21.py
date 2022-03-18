#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
import pandas as pd
import re

pattern = re.compile('Category')
wiki = pd.read_json('jawiki-country.json.gz', lines = True)
uk = wiki[wiki['title'] =='イギリス'].text.values
ls = uk[0].split('\n')
for line in ls:
    if re.search(pattern, line):
        print(line)
