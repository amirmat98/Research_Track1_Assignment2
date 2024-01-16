import rospy
from rt1_a2_2023.msg import TargetPosition
from rt1_a2_2023.srv import LastTarget, Response

PreviousTarget = None

def callback (TempData):
    rospy.loginfo("Last Robot Target Position has been Received")
    global PreviousTarget
    PreviousTarget = TempData

def PreviousTargetImplementation(req):
    res = Response()
    if PreviousTarget:
        res.x = PreviousTarget.x
        res.y = PreviousTarget.y
    else:
        rospy.logwarn("The Target has not been obtained Now.")
    return res

def main():
    rospy.init_node('PreviousTarget')
    rospy.Subscriber("/RobotTarget", TargetPosition, callback)
    rospy.Service('PreviousTarget', LastTarget, PreviousTargetImplementation)
    rospy.loginfo("target node started and ready to give the last target the user entered")
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass