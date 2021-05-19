import numpy as np
import scipy.io as sio
from numpy import double
import src.utils.constants as cte
from src.config.config import Config
from src.format.EventClass import Event
from src.utils.utils import choose, combine, multiInputs, secsToNsecs


# matlab to abstract
def matlabToAbstract(input_file):

    structs_types = list(sio.whosmat(input_file))
    file_data = sio.loadmat(input_file)
    is_matrix = False
    arrays = []
    c = Config()

    # Only one struct
    if len(structs_types) == 1:
        struct_name, struct_size, _ = structs_types[0]

        # 1 struct
        if struct_size == (1, 1):
            struct = file_data[struct_name]

            if c.matlab:
                names = c.config_data["matlab"]["1 struct"]["names"]
            else:
                names = list(map(
                    lambda name: choose("Where is {}?: ".format(name), list(struct.dtype.fields))
                    , cte.MATLAB_STRUCT_NAMES))

            arrays = list(map(
                lambda name: struct[0][name][0]
                , names))

        # Matrix nx4
        elif struct_size[1] == 4:
            is_matrix = True
            matrix = file_data[struct_name]

            if c.matlab:
                indexes = c.config_data["matlab"]["Matrix nx4"]["indexes"]
            else:
                ln = matrix[-1]
                print("The last line of the matrix is [{}, {}, {}, {}]".format(ln[0], ln[1], ln[2], ln[3]))
                indexes = list(map(
                    lambda name: choose("Where is {}?: ".format(name), ln, True)
                    , cte.MATLAB_STRUCT_NAMES))

            arrays = list(map(
                lambda index: matrix[:, index]
                , indexes))

    # 4 structs (one for each event's parameter)
    elif len(structs_types) == 4:
        options = list(map(
            lambda st: st[0]
            , structs_types))

        if c.matlab:
            names = c.config_data["matlab"]["4 structs"]["names"]
        else:
            names = list(map(
                lambda name: choose("Where is {}?: ".format(name), options)
                , cte.MATLAB_STRUCT_NAMES))

        arrays = list(map(
            lambda name: file_data[name]
            , names))

    if is_matrix:
        events = list(map(lambda x, y, pol, ts: Event(x, y, pol, combine(0, ts)), arrays[0], arrays[1], arrays[2], arrays[3]))
    else:
        events = list(map(lambda x, y, pol, ts: Event(x[0], y[0], pol[0], combine(0, ts[0])), arrays[0], arrays[1], arrays[2], arrays[3]))

    return events


# matlab to abstract
def abstractToMatlab(event_list, output_file):
    file_data = {}
    c = Config()

    if c.matlab:
        struct_type = c.config_data["matlab"]["default"]
    else:
        struct_type = choose("Which struct type do you prefer? ", cte.MATLAB_TYPES_ADMITTED)

    arrays = [[], [], [], []]
    for ev in event_list:
        arrays[0].append(double(ev.x))
        arrays[1].append(double(ev.y))
        arrays[2].append(double(ev.pol))
        arrays[3].append(double(secsToNsecs(ev.ts)))

    # 1 struct
    if struct_type == cte.MATLAB_TYPES_ADMITTED[0]:
        if c.matlab:
            struct_name = c.config_data["matlab"]["1 struct"]["struct_name"]
            data_names = c.config_data["matlab"]["1 struct"]["names"]
        else:
            struct_name = input("What is the name of the struct?: ")
            data_names = multiInputs("How are the names of these parameters", cte.MATLAB_STRUCT_NAMES)

        file_data[struct_name] = {}
        for arr, name in zip(arrays, data_names):
            file_data[struct_name][name] = arr

    # Matrix nx4
    elif struct_type == cte.MATLAB_TYPES_ADMITTED[1]:
        if c.matlab:
            struct_name = c.config_data["matlab"]["Matrix nx4"]["struct_name"]
        else:
            struct_name = input("What is the name of the struct?: ")

        file_data[struct_name] = np.column_stack((arrays[0], arrays[1], arrays[2], arrays[3]))

    # 4 structs (one for each event's parameter)
    elif struct_type == cte.MATLAB_TYPES_ADMITTED[2]:
        if c.matlab:
            struct_names = c.config_data["matlab"]["4 structs"]["names"]
        else:
            struct_names = multiInputs("How are the names of these structs", cte.MATLAB_STRUCT_NAMES)

        for arr, name in zip(arrays, struct_names):
            file_data[name] = arr

    sio.savemat(output_file, file_data, oned_as="column")
