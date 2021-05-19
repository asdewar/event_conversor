from src.config.config import Config
from src.conversors.aedatConversorVersions.aedat2Conversor import abstractToAedat2, aedat2ToAbstract
from src.conversors.aedatConversorVersions.aedat3Conversor import abstractToAedat3, aedat3ToAbstract
from src.conversors.aedatConversorVersions.aedat4Conversor import abstractToAedat4, aedat4ToAbstract
from src.utils.utils import choose
import src.utils.constants as cte


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
        version = choose("Choose a version: ", cte.AEDAT_ACCEPTED_VERSIONS)

    if version == cte.AEDAT_ACCEPTED_VERSIONS[0]:
        abstractToAedat2(event_list, output_file)
    elif version == cte.AEDAT_ACCEPTED_VERSIONS[1]:
        abstractToAedat3(event_list, output_file)
    elif version == cte.AEDAT_ACCEPTED_VERSIONS[2]:
        abstractToAedat4(event_list, output_file)
