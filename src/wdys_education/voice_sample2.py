#!/usr/bin/env python
#-*- coding: utf-8 -*-
import roslib
import rospy
from voice_common_pkg.srv import *
import lp_wdys

tts_pub = rospy.ServiceProxy('/tts', TTS)
stt_pub = rospy.ServiceProxy('/stt_server', SpeechToText)
file_name = "question_box.yaml"
file_path = roslib.packages.get_pkg_dir("education") + "/config/" + file_name
lp = lp_wdys.Selector(file_path)

def speak(sentence):
    tts_pub(sentence)
    return

def speechRecog():
    return stt_pub()

def conversation(_dammy):
    ros_response = WhatDidYouSayResponse()
    sentence = speechRecog(short_str=False)
    result_list = lp.checker(sentence.result_str)

    if all(result_list):
        speak("Question is")
        speak(result_list[0])
        speak("Answer is")
        speak(result_list[1])
        ros_response.result = True
    else:
        speak("Sorry I couldn't be recognized")
        ros_response.result = False

    return ros_response

def rosConfig():
    rospy.init_node('voice_sample2')
    rospy.Service('/bf/conversation_srvserver', WhatDidYouSay, conversation)
    rospy.loginfo('Ready to  voice_sample2')
    rospy.spin()

if __name__ == '__main__':
    rosConfig()
