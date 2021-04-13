from src.conversors.matlabConversor import matlabToAbstract, abstractToMatlab
from src.conversors.rosbagConversor import rosbagToAbstract, abstractToRosbag
from src.conversors.textConversor import textToAbstract, abstractToText
from src.utils.utils import raiseException


def convert(input_type, input_file, output_type, output_file):
    event_list = convertToList(input_type, input_file)
    convertWithList(event_list, output_type, output_file)


def convertToList(input_type, input_file):
    switcher = {
        "bag": rosbagToAbstract,
        "mat": matlabToAbstract,
        "txt": textToAbstract
    }

    # Obtenemos la lista de eventos según el input.
    return switcher.get(input_type, lambda: raiseException("Tipo de entrada no admitido"))(input_file)


def convertWithList(event_list, output_type, output_file):
    switcher = {
        "bag": abstractToRosbag,
        "mat": abstractToMatlab,
        "txt": abstractToText
    }

    # La convertimos al archivo que deseemos.
    switcher.get(output_type, lambda: raiseException("Tipo de salida no admitido"))(event_list, output_file)
