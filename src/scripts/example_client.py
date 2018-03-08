#!/data/3knoeppl/bsc_thesis/venvs/hiob/bin/python

import rospy
import hiob_ros.msg


def subscribe():
    print("subscribing...")
    rospy.init_node('hiob_example_client', anonymous=True)
    rospy.Subscriber('/core/objects/0', hiob_ros.msg.TrackingResult, receive_message)


def receive_message(tracking_result):
    print(
        """received result:
    position: [(x:{0.position.x}, y:{0.position.y}), (w:{0.position.w}, h:{0.position.h})]
    prediction quality: {0.predictionQuality}
    loss: {0.lostObject}\n""".format(tracking_result))


if __name__ == '__main__':
    subscribe()
    rospy.spin()