import h5py


def hdf5ToAbstract(input_file):
    file = h5py.File(input_file, 'r')

    file.keys()

    # return events_list


def abstractToHdf5(event_list, output_file):
    pass
