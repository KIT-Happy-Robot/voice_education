#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os.path
import pandas as pd

file_path = os.path.expanduser('~/catkin_ws/src/nlp100/jawiki-country.json.gz')
wiki = pd.read_json(file_path, lines = True)
uk = wiki[wiki['title'] == 'イギリス'].text.values

print(uk)
