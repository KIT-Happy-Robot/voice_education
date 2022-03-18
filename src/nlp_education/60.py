#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
import gensim

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary = True)
print(model['United_States'])
