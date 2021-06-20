from src.converters.mainConverter import getEventsFromFile, putEventsInFile
from src.format.EventClass import Event
import src.config.constants as cte
import src.utils.colors as c
import random
import os

from src.ui.UI import UI

INTERVAL_X = (0, 127)
INTERVAL_Y = (0, 127)
INTERVAL_TS = (0.000000000, 0.000001000)
ERROR_TS = 0.000000002


def equalEvent(event1, event2):
    return (
        event1.x == event2.x and
        event1.y == event2.y and
        event1.pol == event2.pol and
        abs(event1.ts - event2.ts) <= ERROR_TS
    )


def equalEventList(event_list1, event_list2):

    if len(event_list1) != len(event_list2):
        print("Events lists have different size")
        return False

    for ev1, ev2 in zip(event_list1, event_list2):
        if not equalEvent(ev1, ev2):
            print("Failed in events:")
            print(ev1)
            print(ev2)
            return False

    print("Both event lists are equal!!!")
    return True


def getListOfFiles(dir_name):
    list_of_file = os.listdir(dir_name)
    all_files = list()
    for entry in list_of_file:
        full_path = os.path.join(dir_name, entry)
        if os.path.isdir(full_path):
            all_files = all_files + getListOfFiles(full_path)
        else:
            all_files.append(full_path)

    return all_files


def generateRandomEvents(num_events):
    list_events = []
    ts_0 = 0.0

    for _ in range(num_events):

        list_events.append(Event(
            random.randint(INTERVAL_X[0], INTERVAL_X[1]),
            random.randint(INTERVAL_Y[0], INTERVAL_Y[1]),
            random.randint(0, 1) == 1,
            ts_0
        ))

        ts_0 += random.uniform(INTERVAL_TS[0], INTERVAL_TS[1])

    return list_events


def testShuffle(cutoff):
    all_data_files = getListOfFiles(cte.DATA_PATH)
    random.shuffle(all_data_files)

    for file in all_data_files[:cutoff]:
        try:
            type_convert = random.choice(cte.ADMITTED_TYPES)
            testFileAndType(file, type_convert)
        except Exception as err:
            UI().objectUI.errorWindow(err)


def testFileAndType(file_name_1, type_convert):
    c.blue("Testing\n\tfile: {}\n\ttype: {}".format(file_name_1, type_convert))
    file_name_2 = cte.OUTPUT_DEFAULT + type_convert
    event_list_1 = getEventsFromFile(file_name_1)
    putEventsInFile(event_list_1, file_name_2)
    event_list_2 = getEventsFromFile(file_name_2)
    equalEventList(event_list_1, event_list_2)


def testTypes(type1, type2):
    event_list_random = generateRandomEvents(200)
    file1 = cte.OUTPUT_DEFAULT + type1
    file2 = cte.OUTPUT_DEFAULT + type2

    putEventsInFile(event_list_random, file1)
    event_list_1 = getEventsFromFile(file1)
    putEventsInFile(event_list_1, file2)
    event_list_2 = getEventsFromFile(file2)

    equalEventList(event_list_random, event_list_1)
    equalEventList(event_list_random, event_list_2)


def generateRandomFiles(num_events):
    event_list = generateRandomEvents(num_events)
    path = "output/output-test/output-test."
    for t in cte.ADMITTED_TYPES:
        putEventsInFile(event_list, path + t)
