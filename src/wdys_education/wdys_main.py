#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import roslib
import wdys_def
from happymimi_voice_msgs.srv import WhatDidYouSay
from happymimi_voice_msgs.srv import WhatDidYouSayResponse

def main():
    count = 0
    while count != 10:
        print("Ready")
        service = rospy.ServiceProxy('/bf/wdys_sub',WhatDidYouSay)
        ser = service().result
        if  ser:
            count += 1
            print(count)
        else:
            print("one more time")
            



if __name__ == '__main__':
    rospy.init_node('wdys_main')
    main()          
