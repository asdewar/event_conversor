import h5py

from src.format.EventClass import Event
from src.utils.utils import choose


def hdf5ToAbstract(input_file):
    file = h5py.File(input_file, 'r')

    struct_name = choose("Where are stored the events?: ", file.keys())

    data = file[struct_name]['data']
    timestamps = file[struct_name]['timestamp']

    {
        data: [
            [[16, 26, 12],
             [231, 123, 213],
             [9123,133]],
            ...
        ],
        timestamp: [
            100,
            23,
        ]
    }


    # Buscar ts y data preguntando al usuario.

    # Imprimer la primera línea de data para preguntar por el orden.

    # Iterar con los datos obtenidos.

    events_list = []
    i = 0
    j = 0
    k = 0
    for ev_array in data:
        k += 1
        for ev in ev_array:
            i += 1

    for t in timestamps:
        j += 1

    print(i)
    print(j)
    print(k)

    return events_list


def abstractToHdf5(event_list, output_file):
    pass
