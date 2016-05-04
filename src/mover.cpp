#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

#include <sstream>

int main(int argc, char **argv)
{

  ros::init(argc, argv, "mover");

  ros::NodeHandle n;

  ros::Publisher movement_pub = n.advertise<geometry_msgs::Twist>("cmd_vel", 1);

  // We can define a custom rate for our messages here (in Hz)
  ros::Rate loop_rate(10);

  while (ros::ok())
  {
    geometry_msgs::Twist msg;

    float freq = 2.0;

    ros::Time ctime = ros::Time::now();

    msg.linear.x = sin(2*M_PI*freq*ctime.toSec());

    movement_pub.publish(msg);

    ros::spinOnce();

    loop_rate.sleep();
  }


  return 0;
}
