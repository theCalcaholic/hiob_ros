#!/home/tobias/informatics/python/venv/hiob/bin/python
# PYTHONPATH=.. python hy1.py

import os
import rospy


if __name__ == '__main__':
    os.sys.path.append(os.path.dirname(__file__))
    from hiob import hiob_gui
    rospy.init_node("core", anonymous=True)
    hiob_gui.main()
