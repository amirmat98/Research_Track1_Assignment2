#!/usr/bin/env python3

import rospy
from actionlib import SimpleActionClient
from nav_msgs.msg import Odometry
from rt1_a2_2023.msg import PlanningAction, PlanningGoal
from rt1_a2_2023.msg import TargetPosition, Abort, RobotPositionVelocity
import time


if __name__ == '__main__':
    rospy.init_node('DefineTargetService')

    AC = SimpleActionClient('/ReachingGoal', PlanningAction)
    NameSpace = rospy.get_namespace()
    AC.wait_for_server(rospy.Duration(2.0))

    # Subscribers
    TargetSub = rospy.Subscriber('/TargetPosition', TargetPosition, TargetCallback)
    StateSub = rospy.Subscriber('/odom', Odometry, StateCallback)
    AbortSub = rospy.Subscriber('/AbortSub', Abort, AbortCallback)

    # Publishers
    Pub = rospy.Publisher('/RobotPositionVelocity', RobotPositionVelocity, queue_size=10)
    PosTimer = rospy.Timer(rospy.Duration(0.5), TimerCallback)

    rospy.loginfo("Node prepared: Establish Goal")
    rospy.spin()
    rospy.signal_shutdown("Finishing")
    time.sleep(2)

