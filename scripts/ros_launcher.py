import sys
import os
import rospy
import rospkg


if __name__ == '__main__':
    if "--ros-subscribe" not in sys.argv:
        raise Exception("hiob_ros requires the argument '--ros-subscribe <ros node>'. Exiting...")

    if "--ros-publish" not in sys.argv:
        raise Exception("hiob_ros requires the argument '--ros-publish <ros node>'. Exiting...")

    my_path = os.path.realpath(os.path.dirname(__file__))
    os.sys.path.append(my_path)

    rp = rospkg.RosPack()
    config_path = os.path.join(rp.get_path('hiob_ros'), 'config')

    if os.path.isdir(os.path.join(my_path, "..", "..", "..", "src")):
        print("Devel mode detected. Adjusting paths...")
        os.chdir(os.path.join(my_path, '..', 'hiob'))
        config_path = 'config'
        if "-e" not in sys.argv:
            sys.argv.extend(["-e", os.path.join(config_path, 'environment.yaml')])
    else:
        if "-e" not in sys.argv:
            sys.argv.extend(["-e", os.path.join(config_path, 'environment_ros.yaml')])
    if "-t" not in sys.argv:
        sys.argv.extend(['-t', os.path.join(config_path, 'tracker_ros.yaml')])

    rospy.init_node("hiob", anonymous=True)

    if "--no-gui" in sys.argv:
        from hiob import hiob_cli as hiob
        sys.argv.remove('--no-gui')
    else:
        from hiob import hiob_gui as hiob

    hiob.main()
