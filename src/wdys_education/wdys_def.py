#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import roslib
import yaml



file_path = roslib.packages.get_pkg_dir("voice_education") + "/config/" + "question_box.yaml"



def make_QA_list():

    question = []
    answer = []
    with open(file_path) as file:
        obj = yaml.safe_load(file)
        for f in obj:
            question.append(f["Q"])
            answer.append(f["A"])

    return question,answer



