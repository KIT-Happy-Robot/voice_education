#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os.path
import pandas as pd
import re

file_path = os.path.expanduser('~/catkin_ws/src/nlp100/jawiki-country.json.gz')
pattern = re.compile('Category')
wiki = pd.read_json(file_path, lines = True)
uk = wiki[wiki['title'] =='イギリス'].text.values
ls = uk[0].split('\n')
for line in ls:
    if re.search(pattern, line):
        print(line)
