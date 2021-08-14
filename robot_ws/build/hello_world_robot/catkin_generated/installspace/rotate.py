#!/usr/bin/env python2



from geometry_msgs.msg import Twist#for actually moving/rotating robot
from geometry_msgs.msg import Point#for points in 3d space
#from geometry_msgs.msg import Pose#for point/position and QUarternion/orientation in free space
#from nav_msgs.msg import Odometry#dont think I need yet but it uses pose and twist which will for sure come in handy

import rospy


class Rotator():

    def __init__(self):
        self._cmd_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
        #self.pose = Pose() #pose will use QUarternion/orientation and can help orent/ rotate?
        

    def moveFromAToB(self):
        #self.twist = Twist()
        #leaving old code for now
        #r = rospy.Rate(10)
        #while not rospy.is_shutdown():
            #self.twist.angular.z = 0.1
            #self._cmd_pub.publish(self.twist)
            #rospy.loginfo('Rotating robot: %s', self.twist)
            #r.sleep()
        self.twist = Twist()
        goal = Point()
        goal.z = 500
        goal.y = 500
        
        #assuming we're starting from point (0,0)
        z=0.0
        temp=0#testing that my logic makes sense at least
        #y=0#technically only need one of these
        
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            #will rotate the robot so that it's facing diagonally aka 45 degrees but the measurement is 0.7853975 in radians # if this doesn't work figure smt else out
            #pose.orientation perhaps?
            #if self.pose.pose.orientation.x <= 0.7853975:#gunna take another crack at pose later on.
            if temp<=47:
                self.twist.angular.z = 0.1
                rospy.loginfo('Rotating robot: %s', self.twist)
                temp = temp+1
                
            else:
                #need to turn the angular twist off
                self.twist.angular.z = 0
                rospy.loginfo('stopped rotating robot: %s', self.twist)
                z+=0.5
                #y+=0.5# I know I shouldn't do it like this but I couldn't figure out the odometer, I'll try to implement that in lab 2 but this is simpler
                #if past the point stop moving
                
                if goal.z <= z and goal.y <= z:
                    self.twist.linear.z = 0
                    self.twist.linear.y = 0
                    rospy.loginfo('Robot made it to point B: %s', self.twist)
                else:
                    self.twist.linear.x = 0.5#
                    #self.twist.linear.y = 0.5
                    rospy.loginfo('Robot moving to point B: %s', self.twist)
            self._cmd_pub.publish(self.twist)
            r.sleep()


def main():
    rospy.init_node('rotate')
    try:
        rotator = Rotator()
        rotator.moveFromAToB()
    except rospy.ROSInterruptException:
        pass


if __name__ == '__main__':
    main()
