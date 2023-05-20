import rospy
from std_msgs.msg import Int64

def publish_student_id():
    rospy.init_node('publish_student_id', anonymous=True)
    pub = rospy.Publisher('/std_id', Int64, queue_size=10)
    rate = rospy.Rate(10)
    
    student_id = 6352500421
    while not rospy.is_shutdown():
        pub.publish(student_id)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_student_id()
    except rospy.ROSInterruptException:
        pass