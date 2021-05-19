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
    print("Event: x={}\ty={}\tpol={}\tts={}".format(ev.x, ev.y, ev.pol, ev.ts))


def choose(question, options, ret_index=False):
    c.blue("Introduce the INDEX of the element:")
    for i, option in enumerate(options):
        print("[{}] {}".format(i, option))

    try:
        index = int(input(question))
        return index if ret_index else list(options)[index]

    except ValueError:
        c.red('The input must be an integer')
        exit()
    except IndexError:
        c.red('Option out of bounds')
        exit()


def multiInputs(question, options):
    c.blue("Write the NAME for each option:")
    ret_list = []

    print(question)
    for option in options:
        ret_list.append(input("{}: ".format(option)))

    return ret_list


def raiseException(error_text="Error"):
    raise Exception(error_text)


def combine(whole, decimal):
    if decimal == 0:
        return whole
    return whole + (decimal / 1000000000)


def nsecsToSecs(num):
    return num / 1000000000


def secsToNsecs(num):
    return int(num * 1000000000)


def getExtension(file_name):
    return file_name.split(".")[-1]
