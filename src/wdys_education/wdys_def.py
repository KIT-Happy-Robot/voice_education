#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import roslib
import yaml
from happymimi_voice_msgs.srv import TTS
from happymimi_voice_msgs.srv import SpeechToText

tts_pub = rospy.ServiceProxy('/tts', TTS)
stt_pub = rospy.ServiceProxy('/stt_server', SpeechToText)

file_path ="voice_common_pkg/config/rcj2019_whatdidyousay_questions.yaml"

def speechRecog():
    return stt_pub()

def speak(sen):
    tts_pub(sen)

def make_QA_list():

    question = []
    answer = []
    with open(file_path) as file:
        obj = yaml.safe_load(file)
        for f in obj:
            question.append(f["q"])
            answer.append(f["a"])

    return question,answer

def true_false(res,que,ans):
    max_fuz = 0
    num = 0
    for i,q in enumerate(que):
        fuz = fuzz.ratio(res,q)
        if fuz > max_fuz:
            max_fuz = fuz
            num = i
    if max_fuz <= 40:
        return False
    else:
        speak('question is' + que[num])
        speak('answer is' + ans[num])
        return True
