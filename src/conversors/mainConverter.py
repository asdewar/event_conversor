from src.conversors.aedatConversor import aedatToAbstract, abstractToAedat
from src.conversors.binConversor import binToAbstract, abstractToBin
from src.conversors.hdf5Conversor import hdf5ToAbstract, abstractToHdf5
from src.conversors.matlabConversor import matlabToAbstract, abstractToMatlab
from src.conversors.rosbagConversor import rosbagToAbstract, abstractToRosbag
from src.conversors.textConversor import textToAbstract, abstractToText
from src.utils.utils import raiseException, getExtension

switcher = {
        "bag": (rosbagToAbstract, abstractToRosbag),
        "mat": (matlabToAbstract, abstractToMatlab),
        "txt": (textToAbstract, abstractToText),
        "aedat": (aedatToAbstract, abstractToAedat),
        "aedat4": (aedatToAbstract, abstractToAedat),
        "bin": (binToAbstract, abstractToBin),
        "hdf5": (hdf5ToAbstract, abstractToHdf5)
    }


def convert(input_file, output_file, input_type=None, output_type=None):
    event_list = getEventsFromFile(input_file, input_type)
    putEventsInFile(event_list, output_file, output_type)


def getEventsFromFile(input_file, input_type=None):
    if input_type:
        t = input_type
    else:
        t = getExtension(input_file)

    return switcher.get(t, lambda: raiseException("Type of input not admitted"))[0](input_file)


def putEventsInFile(event_list, output_file, output_type=None):
    if output_type:
        t = output_type
    else:
        t = getExtension(output_file)

    switcher.get(t, lambda: raiseException("Type of output not admitted"))[1](event_list, output_file)
