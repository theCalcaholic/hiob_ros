#!/usr/bin/env python
# export MPLBACKEND="agg"
# PYTHONPATH=.. python hy1.py

import os
import rospy


if __name__ == '__main__':
    os.sys.path.append(os.path.dirname(__file__))
    from hiob import hiob_cli
    rospy.init_node("core", anonymous=True)
    hiob_cli.main()
