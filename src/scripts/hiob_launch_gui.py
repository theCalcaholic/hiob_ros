#!/data/3knoeppl/bsc_thesis/venvs/hiob/bin/python
# PYTHONPATH=.. python hy1.py

import os
import rospy

from hiob import hiob_gui

if __name__ == '__main__':
    rospy.init_node("hiob", anonymous=True)
    os.chdir(os.path.join(os.path.dirname(__file__), "hiob"))
    hiob_gui.main()
