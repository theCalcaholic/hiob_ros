#!/data/3knoeppl/bsc_thesis/venvs/hiob/bin/python
# export MPLBACKEND="agg"
# PYTHONPATH=.. python hy1.py

import os
import rospy
from hiob import hiob_cli


if __name__ == '__main__':
    os.chdir("./hiob")
    hiob_cli.main()
