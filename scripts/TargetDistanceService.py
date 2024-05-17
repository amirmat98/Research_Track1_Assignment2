#!/usr/bin/env python3

"""
.. module:: TargetDistanceService
   :platform: Unix
   :synopsis: Node for calculating the relative position and velocity of the robot to its target in the RT1_Second_Assignment project.

.. moduleauthor:: Your Name Here

This module implements a ROS node that calculates the distance and average velocity of a robot relative to a specified target position. The node subscribes to both the robot's current position and velocity and a target position, and provides a service that computes the difference in position and average velocity.
"""

"""

import rospy
from geometry_msgs.msg import Point, Pose, Twist
from nav_msgs.msg import Odometry
import actionlib
import actionlib.msg
import rt1_a2_2023.msg
from rt1_a2_2023.msg import RobotPositionVelocity, TargetPosition
from rt1_a2_2023.srv import LastTarget, LastTargetRequest
from rt1_a2_2023.srv import Mean, MeanResponse
import math



rospy.wait_for_service('last_target')
client = rospy.ServiceProxy('last_target', LastTarget)

# Generate a LastTargetRequest, which is currently an empty request.
request = LastTargetRequest()

velocitys = list()
global  distance
global average_vel_x

"""


def calc_avg(req):
    """
    Service callback function to calculate the average velocity and distance.

    :param req: Service request, not used in this implementation.
    :type req: MeanRequest
    :return: The response containing the distance and average velocity.
    :rtype: MeanResponse
    """
    res = MeanResponse()
    res.dist = distance
    res.velocity_mean = average_vel_x

    return res

def get_avg(msg):
    """
    Subscriber callback function to update distance and average velocity.

    :param msg: The current position and velocity of the robot.
    :type msg: RobotPositionVelocity
    """
    global response, velocitys

    response = client(request)
    target_x = response.x
    target_y = response.y

    window = rospy.get_param('avg_window')
    x_now = msg.x
    y_now = msg.y

    vel_x_now = msg.v_x

    distance = math.sqrt((target_x - x_now)**2 + (target_y - y_now)**2)
    velocitys.append(msg.v_x)

    if (len(velocitys) < window):
        average_vel_x = sum(velocitys) / len(velocitys)
    else:
        average_vel_x = sum(velocitys[-window:]) / window

def main():
    """
    Main function to initialize the ROS node and its subscriptions and services.
    """
    rospy.init_node('RobotToTarget')
    rospy.loginfo("Node operational and prepared to compute the mean")

    rospy.Service('mean', Mean, calc_avg)
    rospy.Subscriber("/kinematics", RobotPositionVelocity, get_avg)

    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass