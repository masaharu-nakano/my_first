#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

cmd_vel = Twist()
cmd_vel.linear.x = 2.0
cmd_vel.angular.z = 0.0

pose = Pose()
nowRotating = False

def update_pose(data):
    global pose
    pose.x = data.x
    pose.y = data.y

def update_cmd_vel():
    global cmd_vel
    global nowRotating
    boundary = 1.0
    if (pose.x < boundary or pose.x > 11.08-boundary or pose.y < boundary or pose.y > 11.08-boundary) and not nowRotating:
        cmd_vel.linear.x = 0.0
        cmd_vel.angular.z = 2.0
        nowRotating = True
    else:
        cmd_vel.linear.x = 2.0
        cmd_vel.angular.z = 0.0
        nowRotating = False

def autonomous_controller():
    rospy.init_node('autonomous_controller')
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('pose', Pose, update_pose)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        update_cmd_vel()
        pub.publish(cmd_vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        autonomous_controller()
    except rospy.ROSInterruptException:
        pass