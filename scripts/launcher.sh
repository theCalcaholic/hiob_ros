#!/usr/bin/env bash

VENV="../venv"


cd "$(dirname "$0")"
source "$VENV/bin/activate"

echo `pwd`

if [ "$1" == "--nogui" ] ; then
  python ./ros_launcher_cli.py
else
  python ./ros_launcher_gui.py
fi
