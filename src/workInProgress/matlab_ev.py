import scipy.io as sio


def comun_a_matlab(eventos, path_file):

    # Guardamos la estructura en un archivo matlab.
    sio.savemat(path_file, {'TD': eventos})


def matlab_a_comun(path_file):
    # file_data = loadmat(full_path)