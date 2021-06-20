from datetime import datetime

# ---------------------- MAIN
ADMITTED_TYPES = ["txt", "bag", "mat", "aedat", "aedat4", "bin"]

CONFIG_PATH = "src/config/config.json"

NUM_PROGRESS_BAR = 100

# ---------------------- TESTING
DATA_PATH = "data"

OUTPUT_DEFAULT = "output."

# ---------------------- MATLAB
MATLAB_STRUCT_NAMES = ['coordinate x', 'coordinate y', 'polarization', 'timestamp']

MATLAB_TYPES_ADMITTED = ['1 struct', 'Matrix nx4', '4 structs']

# ---------------------- AEDAT
AEDAT_ACCEPTED_VERSIONS = ["aedat 2.0", "aedat 3.1", "aedat 4.0"]

INITIAL_COMMENTS_AEDAT2 = ["#!AER-DAT2.0\n", "# This is a raw AE data file - do not edit\n",
                           "# Data format is int32 address, int32 timestamp (8 bytes total), repeated for each event\n",
                           "# Timestamps tick is 1 us\n", "# created " + str(datetime.now()) + '\n']

INITIAL_COMMENTS_AEDAT3 = ["#!AER-DAT3.1\n", "#Format: RAW\n", "#Source 1: DVS128\n",
                           "#Start-Time: " + str(datetime.now()) + '\n', "#!END-HEADER\n"]

INITIAL_COMMENTS_AEDAT4 = ["#!AER-DAT4.0\n"]
