#!/usr/bin/env python
import rospy
from std_srvs.srv import Empty

def handle_hi(req):
    student_name = "<ชื่อของนักศึกษาเอง>"
    rospy.loginfo("Hi, My name is %s", student_name)
    return []

def hi_server():
    rospy.init_node('hi_server')
    rospy.Service('/hi', Empty, handle_hi)
    rospy.loginfo("Ready to say Hi!")
    rospy.spin()

if __name__ == "__main__":
    hi_server()
