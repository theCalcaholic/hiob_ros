#!/usr/bin/env bash


local VENV=""


if [ ! -z $HIOB_VENV ]; then
  local VENV="$HIOB_VENV"
fi

cd "$(dirname "$0")"
source "$HIOB_VENV/bin/activate"

echo `pwd`

if [ "$1" == "--no-gui" ] ; then
  python ./ros_launcher_cli.py
else
  python ./ros_launcher_gui.py
fi
