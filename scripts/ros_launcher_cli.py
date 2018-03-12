import sys
import os
import rospy
import rospkg

#print(str(os.environ))




if __name__ == '__main__':
    os.sys.path.append(os.path.dirname(__file__))
    rp = rospkg.RosPack()
    sys.argv.extend(["-e", os.path.join(rp.get_path('hiob_ros'), 'config', 'environment_ros.yaml'),
                     '-t', os.path.join(rp.get_path('hiob_ros'), 'config', 'tracker.yaml')])
    from hiob import hiob_cli
    rospy.init_node("core", anonymous=True)
    hiob_cli.main()
