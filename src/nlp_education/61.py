#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os.path
import gensim

file_path = os.path.expanduser('~/catkin_ws/src/nlp100/GoogleNews-vectors-negative300.bin.gz')
model = gensim.models.KeyedVectors.load_word2vec_format(file_path, binary=True)
print(model.similarity('United_States', 'U.S.'))
