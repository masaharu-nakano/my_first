#! /usr/bin/env python                                                                         
import rospy
from sensor_msgs.msg import Joy

def joy_callback(joy_msg):
    # ------------- AXES ---------------                                                       
    rospy.loginfo("------------------")
    # XboxOne Analog:left left -1.0 right: 1.0                                                 
    rospy.loginfo("axes0 AN-L LR %s", joy_msg.axes[0])
    # XboxOne Analog:left up 1.0 down: -1.0                                                    
    rospy.loginfo("axes1 AN-L UD: %s", joy_msg.axes[1])
    # XboxOne BackButton L                                                                     
    rospy.loginfo("axes2 BB-L : %s", joy_msg.axes[2])
    # XboxOne Analog:right left -1.0 right: 1.0                                                
    rospy.loginfo("axes3 AN-R LR: %s", joy_msg.axes[3])
    # XboxOne Analog:right up 1.0 down: -1.0                                                   
    rospy.loginfo("axes4 Anl-R UD : %s", joy_msg.axes[4])
    # XboxOne BackButton L                                                                     
    rospy.loginfo("axes5 BB-R UD : %s", joy_msg.axes[5])
    # XboxOne Cross Left:1.0 Right:-1.0                                                        
    rospy.loginfo("axes6 cross LR: %s", joy_msg.axes[6])
    # XboxOne Cross Up:1.0 Down:-1.0                                                           
    rospy.loginfo("axes7 cross  UD: %s", joy_msg.axes[7])
    # ------------- Buttons ---------------                                                    
    rospy.loginfo("buttons0 A %s", joy_msg.buttons[0])
    rospy.loginfo("buttons1 B %s", joy_msg.buttons[1])
    rospy.loginfo("buttons2 X %s", joy_msg.buttons[2])
    rospy.loginfo("buttons3 Y %s", joy_msg.buttons[3])
    rospy.loginfo("buttons4 L %s", joy_msg.buttons[4])
    rospy.loginfo("buttons5 R %s", joy_msg.buttons[5])
    rospy.loginfo("buttons6 CL %s", joy_msg.buttons[6])
    rospy.loginfo("buttons7 CR %s", joy_msg.buttons[7])
    rospy.loginfo("buttons8 X %s", joy_msg.buttons[8])

def start():
    global pub
    rospy.init_node('xbox')
    rospy.Subscriber("joy", Joy, joy_callback, queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    start()