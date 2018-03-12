import sys
import os
import rospy
import rospkg


if __name__ == '__main__':
    os.sys.path.append(os.path.dirname(__file__))
    rp = rospkg.RosPack()
    sys.argv.extend(["-e", os.path.join(rp.get_path('hiob_ros'), 'config', 'environment_ros.yaml'),
                     '-t', os.path.join(rp.get_path('hiob_ros'), 'config', 'tracker.yaml')])
    from hiob import hiob_gui
    rospy.init_node("core", anonymous=True)
    hiob_gui.main()
