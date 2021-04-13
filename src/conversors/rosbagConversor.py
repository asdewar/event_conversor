import rosbag
import rospy
from src.formatFiles.EventClass import Event
from src.utils.colors import *
from src.formatFiles.EventRosbag import Event as _Event
from src.utils.utils import combine, choose


def rosbagToAbstract(input_file):

    bag = rosbag.Bag(input_file)

    topics = bag.get_type_and_topic_info().topics
    topic = choose("Which is the topic that contains the events?: ", topics)

    event_list = []

    for topic, msg, t in bag.read_messages(topics=topic):

        aux_list = []
        if "EventArray" in str(type(msg)):  # msg._type
            aux_list = msg.events
        else:
            aux_list.append(msg)

        for event in aux_list:
            event_list.append(Event(
                event.x,
                event.y,
                event.polarity,
                combine(event.ts.secs, event.ts.nsecs)
            ))

    bag.close()

    return event_list


def abstractToRosbag(event_list, output_file):
    bag = rosbag.Bag(output_file, "w")

    topic_name = input('Introduce the name of the topic where the events are going to be write: ')

    for event in event_list:
        e = _Event()
        e.x = event.x
        e.y = event.y
        e.polarity = event.pol
        e.ts = rospy.Time.from_sec(event.ts)

        bag.write(topic_name, e)

    bag.close()
