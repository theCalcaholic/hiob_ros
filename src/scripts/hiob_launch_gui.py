#!/data/3knoeppl/bsc_thesis/venvs/hiob/bin/python
# PYTHONPATH=../hiob python hy1.py

import os

import hiob_gui

if __name__ == '__main__':
    os.chdir("../hiob")
    hiob_gui.main()
