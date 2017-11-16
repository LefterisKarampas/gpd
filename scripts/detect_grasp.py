import rospy
import tf
from gpd.msg import GraspConfigList

# global variable to store grasps
grasps = []


# Callback function to receive grasps.
def callback(msg):
    global grasps
    grasps = msg.grasps
    if(len(grasps) > 0):
    	br = tf.TransformBroadcaster()
    	br.sendTransform((grasps[0].bottom.x,grasps[0].bottom.y,grasps[0].bottom.z),
                     tf.transformations.quaternion_from_euler(grasps[0].approach.x,
                     	grasps[0].approach.y,
                     	grasps[0].approach.z),
                     rospy.Time.now(),
                     "grasp",
                     "camera_rgb_optical_frame")



# ==================== MAIN ====================
# Create a ROS node.
rospy.init_node('get_grasps')
# Subscribe to the ROS topic that contains the grasps.
sub = rospy.Subscriber('/detect_grasps/clustered_grasps', GraspConfigList, callback)
rospy.spin()
