FROM tensorflow/tensorflow:1.12.0-gpu-py3


SHELL ["/bin/bash", "-c"]
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
ENV HIOB_VENV /opt/hiob_venv
ENV HIOB_ROS_PUBLISH "/hiob/objects/0"
ENV HIOB_ROS_SUBSCRIBE "/ros/videoStream"

RUN echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list \
  && apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116;


# update sources and install packages
RUN apt-get update \
  && apt-get install -y wget ros-kinetic-ros-base git python-virtualenv python3-tk;

RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64.deb \
  && dpkg -i dumb-init_*.deb && rm dumb-init_*.deb

ADD hiob_ros  /tmp/hiob_ros_ws/src/hiob_ros 
ADD hiob_msgs /tmp/hiob_ros_ws/src/hiob_msgs
RUN virtualenv -p python3 --system-site-packages "$HIOB_VENV" \
  && "$HIOB_VENV/bin/pip" install -r /tmp/hiob_ros_ws/src/hiob_ros/hiob/requirements.txt \
  && apt-get remove python-virtualenv -y && apt-get autoremove -y
RUN cd /tmp/hiob_ros_ws/ \
  && /opt/ros/kinetic/env.sh catkin_make install -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
  && rm -rf /tmp/hiob_ros_ws \
  && chmod +rx /opt/ros/kinetic/setup.bash && ls -l /opt/ros/kinetic/setup.bash;


CMD ["bash", "-c", ". /opt/ros/kinetic/setup.bash; ([ \"$RUN_ROSCORE\" == \"true\" ] && exec roscore &); (exec rosrun hiob_ros launcher --python \"$HIOB_VENV/bin/python\" --ros-subscribe $HIOB_ROS_SUBSCRIBE --ros-publish $HIOB_ROS_PUBLISH)"]
