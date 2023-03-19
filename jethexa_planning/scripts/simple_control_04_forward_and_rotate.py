#!/usr/bin/env python3
# coding: utf-8

import time
import rospy
import nav_msgs.msg as nav_msgs
from scipy.spatial.transform import Rotation as R
from geometry_msgs.msg import Quaternion, Point, Vector3, TransformStamped, TwistWithCovarianceStamped
#
from jethexa_controller_interfaces import msg as jetmsg
from jethexa_controller_interfaces.msg import Traveling
from jethexa_controller_interfaces.srv import SetPose1, SetPose1Request, SetPose1Response
from jethexa_controller_interfaces.srv import SetPose2, SetPose2Request, SetPose2Response
from jethexa_controller_interfaces.srv import PoseTransform, PoseTransformRequest, PoseTransformResponse
#
from jethexa_controller import jethexa, build_in_pose, config
from jethexa_controller.z_voltage_publisher import VoltagePublisher
from jethexa_controller.z_joint_states_publisher import JointStatesPublisher
import geometry_msgs.msg

def Traveling_Publisher():
    rospy.init_node("moving_node",anonymous=True,log_level=rospy.INFO)
    pub = rospy.Publisher('/jethexa_controller/traveling', jetmsg.Traveling ,queue_size = 10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
      msg= jetmsg.Traveling()
      msg.gait=2;
      msg.stride=30.0;
      msg.height=20.0;
      msg.direction=0;
      msg.rotation=0.0;
      msg.time=1;
      msg.steps=30;
      msg.relative_height=False;
      msg.interrupt=False;

      pub.publish(msg)
      rate.sleep()
if __name__=="__main__":
  try:
       Traveling_Publisher()
  except rospy.ROSInterruptException:
       pass

    









    
  
    

