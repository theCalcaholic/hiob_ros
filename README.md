# HIOB-ROS

## Description

Provides the [HIOB-Tracker](https://github.com/kratenko/HIOB) 
as ROS-node (network service) which can receive a video stream
and track any given object therein.

__Note:__ _This is only a server application, you need to use or write a
client to make use of it. An example client is being provided
[here](https://github.com/theCalcaholic/hiob_example_client)._

## Requirements
- Python >= 3.5
- A ros distribution (Kinetic or above)
- (optional, required for GPU support) CUDA and CUDNN versions 
    compatible with your desired Tensorflow version
    (e.g. CUDA 9.0 + CUDNN 7.0.5 for Tensorflow 1.6.0) 

##  Installation

---------------------
_The fastest way to run HIOB as a ROS service is via the provided docker image.
If you want to do so you can skip this section and continue directly with the [**Usage**](#usage) section._

---------------------

Assuming that you have already installed the Requirements (see above),
these are the steps for installing HIOB-ROS from the terminal:

1. Source the ros setup script, e.g.
    ```sh
    . /opt/ros/kinetic/setup.bash
    ```
2. Create or reuse a directory for a ros workspace and change to it, e.g.
    ```sh
    mkdir hiob_ros_ws
    cd hiob_ros_ws
    ```
3. Clone HIOB-ROS and depending ROS packages (use `--recurse-submodules`!)
    ```sh
    clone --recurse-submodules https://github.com/theCalcaholic/hiob_ros.git
    clone https://github.com/theCalcaholic/hiob_msgs.git
    ```
4. Install the ROS packages with catkin
    ```sh
    catkin_make install
    ```
5. Setup a virtual environment for HIOB - this needs to be
    __outside__ of the ros workspace (this step is explained in-depth in
    the [HIOB repository](https://github.com/kratenko/HIOB/blob/master/README.md)), e.g.
    ```
    virtualenv -p python3 ../hiob_venv
    . ../hiob_venv/bin/activate
    pip install -r hiob_ros/hiob/requirements.txt
    # or: pip install -r hiob_ros/hiob/requirements_cpu.txt
    ```

Now you should be able to continue with the [**Usage**](#Usage) section.

## Usage

#### Running HIOB-ROS via Docker

The fastest way to run docker is running the [docker image](https://hub.docker.com/r/thecalcaholic/hiob_ros/).
In order to do so, you need to setup [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) first and then run the
image, for example:

```
docker run -e RUN_ROSCORE=true -e HIOB_ROS_SUBSCRIBE=/hiob_client/myTopic -e HIOB_ROS_PUBLISH=/hiob/object --network="host" --runtime=nvidia --rm thecalcaholic/hiob_ros:latest
```
This will download and run hiob_ros from the docker hub. If `-e RUN_ROSCORE=true` is being provided, a roscore
node will be started together with the HIOB server. The latter will then listen on the topic `/hiob_client/myTopic`
for images and publish the object position to `/hiob/object`.

The command above acts (for network purposes) like it was run on the host natively (because of `--network="host"`)
which is the easiest way to spin up a ros server, but might not be your best option, if you want to host the server
continuously (if you require a different port/network setup, refer to
[the networking section of the docker docs](https://docs.docker.com/network/)).

If you have roscore already running on another machine or on the host directly, you can remove the
parameter `-e RUN_ROSCORE=true` and specify a core URI (only necessary if running roscore somewhere else than on the
host or if not using `--network="host"`) by adding `-e ROS_MASTER_URI=http://roscore-address:port/` instead.  
 

#### Running HIOB-ROS Natively

_This section assumes that you have followed the steps in [**Installation**](#Installation) section carefully._

If so, you should be able to follow these steps in order to run HIOB-ROS:

1. Source the ros setup scripts of both the ros distro and your ros workspace, e.g.
    ```sh
    . /opt/ros/kinetic/setup.bash
    . ./hiob_ros_ws/install/setup.bash
    ```    
2. Start an instance of roscore
    ```sh
    roscore
    ```
3. Open a new terminal window and repeat step 1. 
4. Enable the virtual environment you created earlier. _This step is
    optional, as you can also pass the path to the python interpreter
    to hiob via the `--python` parameter._ E.g.
    ```sh
    . ../hiob_venv/bin/activate
    ```
5. Run HIOB-ROS
    ```sh
    rosrun hiob_ros launcher --ros-subscribe </ros/subscribe_topic_name> --ros-publish </ros/publish_topic_name>
    ```
    `</ros/{subscribe|publish}_topic_name>` are placeholders for the topics you want to have
    HIOB subscribe/publish to. These can technically be any strings that comply to the
    [naming convention for ros graph resource names](https://wiki.ros.org/Names#Valid_Names) and need to be equal
    between server and your client.