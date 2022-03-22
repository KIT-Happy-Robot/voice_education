#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import roslib
import wdys_def
from happymimi_voice_msgs.srv import SpeechToText
from happymimi_voice_msgs.srv import SpeechToTextResponse
from happymimi_voice_msgs.srv import TTS
from happymimi_voice_msgs.srv import TTSResponse
from happymimi_voice_msgs.srv import WhatDidYouSay
from happymimi_voice_msgs.srv import WhatDidYouSayResponse
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from happymimi_msgs.srv import StrTrg


tts_pub = rospy.ServiceProxy('/tts', StrTrg)
stt_pub = rospy.ServiceProxy('/stt_server', SpeechToText)



def que_ans(_dammy):
    a = WhatDidYouSayResponse()
    (que,ans) = wdys_def.make_QA_list()
    result_01 = stt_pub().result_str
    res = str(result_01)
    max_fuz = 0
    num = 0
    for i,q in enumerate(que):
        fuz = fuzz.ratio(res,q)
        if fuz > max_fuz:
            max_fuz = fuz
            num = i
    if max_fuz <= 40:
        a.result =  False
    else:
        print(res)
        tts_pub('question is' + que[num])
        tts_pub("answer is" + ans[num])
        a.result = True
        
    return a

def config():
    rospy.init_node('wdys_sub')
    rospy.Service('/bf/wdys_sub',WhatDidYouSay,que_ans)
    rospy.loginfo('Ready to wdys_sub')
    rospy.spin()



if __name__ == '__main__':
    config()


