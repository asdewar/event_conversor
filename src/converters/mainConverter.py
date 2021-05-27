from src.converters.aedatConverter import aedatToAbstract, abstractToAedat
from src.converters.binConverter import binToAbstract, abstractToBin
from src.converters.matlabConverter import matlabToAbstract, abstractToMatlab
from src.converters.rosbagConverter import rosbagToAbstract, abstractToRosbag
from src.converters.textConverter import textToAbstract, abstractToText
from src.utils.utils import getExtension, checkPathAndType, addExtension

switcher = {
        "bag": (rosbagToAbstract, abstractToRosbag),
        "mat": (matlabToAbstract, abstractToMatlab),
        "txt": (textToAbstract, abstractToText),
        "aedat": (aedatToAbstract, abstractToAedat),
        "aedat4": (aedatToAbstract, abstractToAedat),
        "bin": (binToAbstract, abstractToBin)
    }


def convert(input_file, output_file, input_type="", output_type=""):
    event_list = getEventsFromFile(input_file, input_type)
    putEventsInFile(event_list, output_file, output_type)


def getEventsFromFile(input_file, input_type=""):
    if input_type != "":
        t = input_type
    else:
        t = getExtension(input_file)

    checkPathAndType(input_file, t)

    f = switcher.get(t, None)
    if t:
        return f[0](input_file)
    else:
        raise Exception("Type of input ({}) not admitted".format(t))


def putEventsInFile(event_list, output_file, output_type=""):
    if output_type != "":
        t = output_type
    else:
        t = getExtension(output_file)

    addExtension(output_file, t)

    f = switcher.get(t, None)
    if t:
        return f[1](event_list, output_file)
    else:
        raise Exception("Type of output ({}) not admitted".format(t))
