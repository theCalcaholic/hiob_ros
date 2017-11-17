#!/data/3knoeppl/bsc_thesis/venvs/hiob/bin/python
# export MPLBACKEND="agg"
# PYTHONPATH=.. python hy1.py

import sys


venv_libs = "/data/3knoeppl/bsc_thesis/venvs/hiob/lib/python3.5/site-packages/"
sys.path.insert(0, venv_libs)
#sys.path.remove("/opt/ros/kinetic/lib/python2.7/dist-packages")
import os
import rospy
from hiob import hiob_cli


if __name__ == '__main__':
    os.chdir(os.path.join(os.path.dirname(__file__), "hiob"))
    hiob_cli.main()
