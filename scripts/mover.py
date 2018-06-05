#! /usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist

def mover():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)
    vel = Twist()
    freq = 0.2
    while not rospy.is_shutdown():
        vel.linear.x = math.sin(2*math.pi*freq*rospy.get_time())
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        mover()
    except rospy.ROSInterruptException:
        pass
