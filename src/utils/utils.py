from math import floor, log10

import src.utils.colors as c


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