#! /usr/bin/env python3
"""
.. module:: TargetPositionService
   :platform: Unix
   :synopsis: Tracking and reporting the final objective location of the robot as part of the RT1_Second_Assignment project using a node.

.. moduleauthor:: Amirmahdi Matin

The last known target position received by the robot is returned via a service provided by a ROS node implemented in this module. The last position received by the node, which is maintained and queried via a ROS service, is subscribed to for target position updates.
"""

import rospy
from rt1_a2_2023.msg import TargetPosition
from rt1_a2_2023.srv import LastTarget, LastTargetResponse


PreviousTarget = None

def callback (TempData):
    """
    Callback function for the TargetPosition subscriber.

    :param TempData: the last position data received
    :type TempData: TargetPosition
    """
    rospy.loginfo("Last Robot Target Position has been Received")
    global PreviousTarget
    PreviousTarget = TempData

def PreviousTargetImplementation(req):
    """
    Service handler to provide the last known target position.

    :param req: The request object (empty for this service)
    :type req: LastTargetRequest
    :returns: The last known target position, if available
    :rtype: LastTargetResponse
    """
    res = LastTargetResponse()
    if PreviousTarget:
        res.x = PreviousTarget.x
        res.y = PreviousTarget.y
    else:
        rospy.logwarn("The Target has not been obtained Now.")
    return res

def main():
    """
    Main function to initialize the ROS node and service.
    """
    rospy.init_node('LastTarget')
    rospy.Subscriber("/TargetPosition", TargetPosition, callback)
    rospy.Service('LastTarget', LastTarget, PreviousTargetImplementation)
    rospy.loginfo("target node started and ready to give the last target the user entered")
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass