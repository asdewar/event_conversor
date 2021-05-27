from src.utils.utils import getNumProgress
from src.format.EventClass import Event
from src.gui.UI import UI


def textToAbstract(input_file):
    UI().objectUI.showMessage("Starting to read txt file", "w")
    events = open(input_file).readlines()
    events_list = []

    num_progress = getNumProgress(len(events))
    for i, event in enumerate(events):
        if i % num_progress == 0:
            UI().objectUI.sumProgress()

        data = event.strip('\n').split(' ')
        events_list.append(Event(
            int(data[1]),         # Integer
            int(data[2]),         # Integer
            int(data[3]) == 1,    # Boolean
            float(data[0])        # Double
        ))
    UI().objectUI.sumProgress(True)
    UI().objectUI.showMessage("Finishing reading the txt file", "c")
    return events_list


def abstractToText(event_list, output_file):
    UI().objectUI.showMessage("Starting to write txt file", "w")
    f = open(output_file, "w")

    num_progress = getNumProgress(len(event_list))
    for i, event in enumerate(event_list):
        if i % num_progress == 0:
            UI().objectUI.sumProgress()

        f.write("{:.9f} {} {} {}\n".format(
            event.ts,
            event.x,
            event.y,
            int(event.pol),
        ))
    UI().objectUI.sumProgress(True)
    f.close()
    UI().objectUI.showMessage("Finishing writing the txt file", "c")
