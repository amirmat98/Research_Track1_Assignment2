#!/usr/bin/env python3

"""
.. module:: DefineActionClient
   :platform: Unix
   :synopsis: DefineActionClient node for the RT1_Second_Assignment project

.. moduleauthor:: Amirmahdi Matin

Implementing a Python node that executes an action client, which coordinates the movement of the automaton towards a point specified by the user.
The bug_0 algorithm was built with this objective in mind.


Subscribers:
    /pos_and_vel -> The position, linear velocity along the x-axis, and angular velocity about the z-axis of the automaton are obtained and printed via a custom message.



Publishers:
   /odom -> current position, velocity, and additional odometry data of the robot
   /reaching_goal/result -> Present state of the robot

Action client topic:
   /reaching_goal -> employed to establish communication with the "bug_as" action server.
"""

"""
import rospy
from geometry_msgs.msg import Point, Pose, Twist
from nav_msgs.msg import Odometry
import actionlib
import actionlib.msg
from rt1_a2_2023.msg import PlanningAction, PlanningGoal
from rt1_a2_2023.msg import TargetPosition, Abort, RobotPositionVelocity
import timgeometry_msgs.e
import sys
import select
import os
from std_srvs.srv import *
from rt1_a2_2023.srv import LastTarget, RobotToTarget
"""


# global variables
global temp_status
global have_goal
global goal_reached


def publish_message(msg):
    """
    This function outputs the message *pos_and_vel*, which is custom-defined.

    Args:
    msg(Odometry): the velocity and position of the robot
    """
    # get the current position of the robot from the msg in the topic /odom.
    position = msg.pose.pose.position
    linear_velocity = msg.twist.twist.linear

    #define the message that will be published
    pos_vel = RobotPositionVelocity()
    pos_vel.x = position.x
    pos_vel.y = position.y
    pos_vel.v_x = linear_velocity.x
    pos_vel.v_y = linear_velocity.y

    # publish the message
    publisher.publish(pos_vel)

def idle():
    """ First status of the dictionary used to implement a switch-case structure in the *robot_status()* function
    """
    rospy.loginfo("Idle")
    # get the current goal from the parameters in the launch file
    x_t = rospy.get_param('/des_pos_x')
    y_t = rospy.get_param('/des_pos_y')

    rospy.loginfo("Current goal is: x = %f, y = %f", x_t, y_t)

    #define the new goal based on the default goal that is defined in the launch file
    goal_new = rt1_a2_2023.msg.PlanningGoal()
    goal_new.target_pose.pose.position.x = x_t
    goal_new.target_pose.pose.position.y = y_t

    # send the new goal to the action server
    action_client.send_goal(goal_new)
    # change the status
    temp_status = 1
    have_goal = 1

def going_to_goal():
    """ Second status of the dictionary used to implement a switch-case structure in the *robot_status()* function
    """
    rospy.loginfo("Going to goal")
    display_command()
    # ask the user for the command
    input_command = input("which command? \n")
    if input_command == 'c':
        if have_goal:
            # cancel the goal first
            have_goal = 0
            action_client.cancel_goal()
            rospy.loginfo("Goal canceled")
            # get the new goal from the client
            input_x = float(input("enter the x coordinate: "))
            input_y = float(input("enter the y coordinate: "))
            # change the goal and send it to the action server
            rospy.loginfo("New goal is: x = %f, y = %f", input_x, input_y)
            rospy.set_param('/des_pos_x', input_x)
            rospy.set_param('/des_pos_y', input_y)
            goal_new.target_pose.pose.position.x = input_x
            goal_new.target_pose.pose.position.y = input_y

            # send new goal to the action server
            action_client.send_goal(goal_new)
            have_goal = 1
    elif input_command == 'q':
        if have_goal:
            # cancel the goal
            have_goal = 0
            action_client.cancel_goal()
            rospy.loginfo("Goal canceled")
        elif not have_goal:
            rospy.loginfo("No goal to cancel")
    else:
        rospy.loginfo("Invalid command")

    

def change_goal():
    rospy.loginfo("Change goal")

def default():
    """ Default status of the dictionary used to implement a switch-case structure in the *robot_status()* function. It corresponds to an error case.
    """
    rospy.loginfo("Default")


def switch_status(case):
    switch_dictionary = {
        0: idle,
        1: going_to_goal,
        2: change_goal
    }

    # call the function according to the case
    switch_dictionary.get(case, default)()


def robot_status():
    """
    This function controls every action performed by the primary robot.
    """
    temp_status = 0
    rospy.loginfo("Robot status is idle")
    
    while not rospy.is_shutdown():
        switch_status(temp_status)

def display_command():
    print("--------------------------------\n")
    print("the Robot is going to the goal\n")
    print("choose one of the following options:\n")
    print("change goal: c\n")
    print("cancel goal: q\n")
    print("--------------------------------\n")


if __name__ == '__main__':
    try:
        # Initialize the node
        rospy.init_node('DefineActionClient')

        # log the initialization of the node
        rospy.loginfo("Node initialized successfully")

        # Initialize the publisher
        global publisher
        publisher = rospy.Publisher("/RobotPositionVelocity", RobotPositionVelocity, queue_size=1)
        """ 
        The message publisher is responsible for generating the position and velocity of the robot along designated axes.
	    """

        # Initialize the subscriber
        global subscriber
        subscriber = rospy.Subscriber("/odom", Odometry, publish_message)
        """
        Odometry subscriber for the robot's position and velocity.
        """

        # Initialize the action client
        global action_client
        action_client = actionlib.SimpleActionClient('/reaching_goal', rt1_a2_2023.msg.PlanningAction)
        action_client.wait_for_server()
        rospy.loginfo("Action client initialized successfully")
        """
        Action client initialing
        """
    
        # Call the robot status function
        robot_status()


    
    except rospy.ROSInterruptException:
        print("Program interrupted before completion", file=sys.stderr)

