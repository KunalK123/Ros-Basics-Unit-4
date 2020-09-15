#! /usr/bin/env python
import rospy
import math

from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
def callback(msg):
	if msg.ranges[360] > 1 or math.isnan(msg.ranges[360]):
	    move.linear.x = 0.2
      move.angular.z = 0.0
	if msg.ranges[360] < 1: 
	    move.linear.x = 0.0
	    move.angular.z = 0.2
	if msg.ranges[635] < 0.3:
      move.linear.x = 0.0
	    move.angular.z = -0.2
  if msg.ranges[0] < 0.3:
	    move.linear.x = 0.0
	    move.angular.z = 0.2
      
pub.publish(move)
rospy.init_node("topics_quiz_node")
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 1)
move = Twist()
rospy.spin()
