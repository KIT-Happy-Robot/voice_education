#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
import gensim

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)

print(model.most_similar('United_States', topn = 10))
