#! /usr/bin/env python
import rospy
import math
import sys
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class controller:
    def __init__(self):
        self.pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        self.sub = rospy.Subscriber('scan', LaserScan, self.callback, queue_size=1)

    def callback(self, data):
        vel = Twist()
        idx = int(math.floor(0.5*(data.angle_max-data.angle_min)/data.angle_increment))
        limit = int(0.25*math.pi/data.angle_increment)
        print limit
        dsum = 0.0
        nmeas = 0
        for i in range(idx-limit, idx+limit):
            if not math.isinf(data.ranges[i]) and not math.isnan(data.ranges[i]):
                dsum = dsum + data.ranges[i]
                nmeas = nmeas + 1
        dist = dsum / float(nmeas);
        print "Distance to obstacle: " + str(dist)
        if dist > 5.0 and not math.isnan(dist) and not math.isinf(dist):
            vel.linear.x = 0.5
            vel.angular.z = 0.0
        else:
            vel.linear.x = 0.0
            vel.angular.z = 0.5
          
        self.pub.publish(vel)


def main(args):   
    rospy.init_node('ddrcontrol', anonymous=True)
    cl = controller()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down node"

if __name__ == '__main__':
    main(sys.argv)
