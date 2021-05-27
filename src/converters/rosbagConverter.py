from src.utils.utils import combine, getNumProgress
from src.format.EventRosbag import Event as _Event
from src.format.EventClass import Event
from src.config.config import Config
from src.gui.UI import UI
import rosbag
import rospy


def rosbagToAbstract(input_file):
    UI().objectUI.showMessage("Starting to read bag file", "w")
    bag = rosbag.Bag(input_file)
    c = Config()

    if c.rosbag:
        topic = c.config_data["rosbag"]["topic"]
    else:
        topics = bag.get_type_and_topic_info().topics
        topic = UI().objectUI.chooseWindow("Which is the topic that contains the events?: ", topics)

    event_list = []

    num_progress = getNumProgress(bag.get_message_count(topic))
    i = 0
    for topic, msg, t in bag.read_messages(topics=topic):

        if i % num_progress == 0:
            UI().objectUI.sumProgress()
        i += 1

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
    UI().objectUI.sumProgress(True)
    UI().objectUI.showMessage("Finishing reading the bag file", "c")
    return event_list


def abstractToRosbag(event_list, output_file):
    UI().objectUI.showMessage("Starting to write bag file", "w")
    bag = rosbag.Bag(output_file, "w")
    c = Config()

    if c.rosbag:
        topic = c.config_data["rosbag"]["topic"]
    else:
        topic = UI().objectUI.simpleInput("Introduce the name of the topic where the events are going to be write: ")

    num_progress = getNumProgress(len(event_list))
    for i, event in enumerate(event_list):
        if i % num_progress == 0:
            UI().objectUI.sumProgress()

        e = _Event()
        e.x = event.x
        e.y = event.y
        e.polarity = event.pol
        e.ts = rospy.Time.from_sec(event.ts)

        bag.write(topic, e)

    UI().objectUI.sumProgress(True)
    bag.close()
    UI().objectUI.showMessage("Finishing writing the bag file", "c")
