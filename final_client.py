#!/usr/bin/env python
import rospy
from std_srvs.srv import Empty

def call_hi_service():
    rospy.wait_for_service('/hi')
    try:
        hi_service = rospy.ServiceProxy('/hi', Empty)
        hi_service()
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", str(e))

if __name__ == "__main__":
    rospy.init_node('hi_client')
    call_hi_service()
