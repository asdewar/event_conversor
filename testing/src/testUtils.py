import random
from src.conversors.mainConverter import convertWithList, convertToList
from src.formatFiles.EventClass import Event
from src.utils.utils import printEvent

NUM_EVENTS = 50
INTERVAL_X = (0, 500)
INTERVAL_Y = (0, 500)
INTERVAL_TS = (0.000000000, 0.000010000)

ERROR_TS = 0.000000002

TEST_FILE = "testing/output/test_output."


def testGenerateRandomEvents():

    list_events = []
    ts_0 = 0.0

    for _ in range(NUM_EVENTS):

        list_events.append(Event(
            random.randint(INTERVAL_X[0], INTERVAL_X[1]),
            random.randint(INTERVAL_Y[0], INTERVAL_Y[1]),
            random.randint(0, 1) == 1,
            ts_0
        ))

        ts_0 += random.uniform(INTERVAL_TS[0], INTERVAL_TS[1])

    return list_events


def testSaveEventsByType(event_list, output_type, output_file=None):
    convertWithList(event_list, output_type, output_file if output_file else TEST_FILE + output_type)


def testLoadEventsByFile(input_type, input_file=None):
    return convertToList(input_type, input_file if input_file else TEST_FILE + input_type)


def equalEventList(event_list1, event_list2):

    if len(event_list1) != len(event_list2):
        print("Events lists have different size")
        return False

    for ev1, ev2 in zip(event_list1, event_list2):
        if not equalEvent(ev1, ev2):
            print("Failed in events:")
            printEvent(ev1)
            printEvent(ev2)
            return False

    print("Both event lists are equal!!!")
    return True


def equalEvent(event1, event2):
    return (
        event1.x == event2.x and
        event1.y == event2.y and
        event1.pol == event2.pol and
        abs(event1.ts - event2.ts) <= ERROR_TS
    )
