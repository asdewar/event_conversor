from src.converters.aedatConverterVersions.aedat2Converter import abstractToAedat2, aedat2ToAbstract
from src.converters.aedatConverterVersions.aedat3Converter import abstractToAedat3, aedat3ToAbstract
from src.converters.aedatConverterVersions.aedat4Converter import abstractToAedat4, aedat4ToAbstract
from src.config.config import Config
import src.utils.constants as cte
from src.gui.UI import UI


def aedatToAbstract(input_file):
    f = open(input_file, "rb")

    first_line = f.readline().strip()

    if first_line == "#!AER-DAT2.0".encode():
        return aedat2ToAbstract(input_file)
    elif first_line == "#!AER-DAT3.1".encode():
        return aedat3ToAbstract(input_file)
    elif first_line == "#!AER-DAT4.0".encode():
        return aedat4ToAbstract(input_file)


def abstractToAedat(event_list, output_file):
    c = Config()

    if c.aedat:
        version = c.config_data["aedat"]["version"]
    else:
        version = UI().objectUI.chooseWindow("Choose a version: ", cte.AEDAT_ACCEPTED_VERSIONS)

    if version == cte.AEDAT_ACCEPTED_VERSIONS[0]:
        abstractToAedat2(event_list, output_file)
    elif version == cte.AEDAT_ACCEPTED_VERSIONS[1]:
        abstractToAedat3(event_list, output_file)
    elif version == cte.AEDAT_ACCEPTED_VERSIONS[2]:
        abstractToAedat4(event_list, output_file)
