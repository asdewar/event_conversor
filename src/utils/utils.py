import os
import src.utils.colors as c


def checkPathAndType(path, file_types):
    if not os.path.exists(path):
        c.red("Path doesn't exist")
        exit()

    file_type = path.split(".")[-1]
    if file_type not in file_types:
        c.red("This type of file isn't admitted (only {})".format(file_types))
        exit()

    return file_type


def printEvent(ev):
    print("Event: x={}\ty={}\tpol={}\tts={}".format(ev['x'], ev['y'], ev['pol'], ev['ts']))


def choose(question, options):

    c.blue("---CHOOSE---")
    for i, option in enumerate(options):
        print("[{}] {}".format(i, option))

    try:
        index = int(input(question))
        return list(options)[index]

    except ValueError:
        c.red('The input must be an integer')
        exit()
    except IndexError:
        c.red('Option out of bounds')
        exit()


def raiseException(error_text="Error"):
    raise Exception(error_text)


def combine(a, b):
    if b == 0:
        return a
    return a + (b / 1000000000)