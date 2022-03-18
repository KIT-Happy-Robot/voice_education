#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
import pandas as pd

wiki = pd.read_json('jawiki-country.json.gz', lines = True)
uk = wiki[wiki['title'] == 'イギリス'].text.values

print(uk)
