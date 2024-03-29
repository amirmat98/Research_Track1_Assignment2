#!/usr/bin/env python3

import rospy
from rt1_a2_2023.msg import RobotPositionVelocity, TargetPosition
from rt1_a2_2023.srv import RobotToTarget, RobotToTargetResponse
import math

TargetFlag = False
AvgVelWin = rospy.get_param('Avg_Vel_Win', default = 20)
Robot = RobotPositionVelocity()
Target = TargetPosition()
Velocities = []


def TargetPosCallback(data):
    global TargetFlag, Target
    Target.x = data.x
    Target.y = data.y
    TargetFlag = True

def RobotPosVeCallback(data):
    global Velocities
    Robot.x_pos = data.x
    Robot.y_pos = data.y
    if len(Velocities) < AvgVelWin:
        Velocities.append( (data.v_x, data.v_y) )
    elif len(Velocities) == AvgVelWin:
        Velocities.pop(0)
        Velocities.append((data.v_x, data.v_y))

def RobotToTargetCallback(req):
    response = RobotToTargetResponse()
    global TargetFlag, Target, Robot, Velocities

    if TargetFlag:
        response.d_x = Target.x - Robot.x_pos
        response.d_y = Target.y - Robot.y_pos
        rospy.loginfo("Target Position X: %d Target Position Y: %d", Target.x, Target.y)
        response.distance = math.sqrt( (Target.x - Robot.x_pos)**2 + (Target.y - Robot.y_pos)**2 )

    else:
        response.d_x = 0
        response.d_y = 0

    response.average_v_x = sum(x[0] for x in Velocities) / len(Velocities)
    response.average_v_y = sum(y[0] for y in Velocities) / len(Velocities)

    return response




def main():
    rospy.init_node('RobotToTarget', anonymous=False)
    rospy.Subscriber("/TargetPosition", TargetPosition, TargetPosCallback)
    rospy.Subscriber("/RobotPositionVelocity", RobotPositionVelocity, RobotPosVeCallback)
    rospy.Service("RobotToTarget", RobotToTarget, RobotToTargetCallback)
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass