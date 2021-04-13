# External imports.
import sys
import argparse
import scipy.io as sio

# My imports.
from src.formatFiles.EventClass import Event
from src.utils.colors import *
from src.utils.utils import choose

STRUCT_NAMES = ['x', 'y', 'ts', 'pol']


# matlab to abstract
def matlabToAbstract(input_file):
    # Cargamos el formato del archivo.
    format = sio.whosmat(input_file)

    # Cargamos el archivo.
    data = sio.loadmat(input_file)

    # Si hay solo una estructura y es de tamalo 1x1, es una estructura con 4 arrays.
    if len(format) == 1 and format[0][1] == (1, 1):

        # Obtenemos la estructura.
        struct = data[format[0][0]]

        # Obtenemos los nombres de los 4 arrays.
        options = list(struct.dtype.fields)

        # Obtenemos el orden de los arrays.
        names = list(map(
            lambda name: choose("¿Donde se encuentra {}?: ".format(name), options)
            , STRUCT_NAMES))

        # Obtenemos los arrays
        arrays = list(map(
            lambda name: struct[0][name][0]
            , names))

    # Si es solo una estructura, pero no de tamaño 1x1, hay 
    elif len(format) == 1 and format[0][1] != (1, 1):
        print("·PROCESO")

    # Si hay cuatro estructuras, eso significa que hay 4 estructuras con x, y, pol y ts .
    elif len(format) == 4:

        # Se obtienen los nombres de todos los arrays del archivo.
        options = list(map(
            lambda st: st[0]
            , format))

        # Le preguntamos al usuario que estructuras de las que hay quiere.
        names = list(map(
            lambda name: choose("¿Donde se encuentra {}?: ".format(name), options)
            , STRUCT_NAMES))

        # Cargamos cada array según su nombre.
        arrays = list(map(
            lambda name: data[name]
            , names))

    # Creamos el diccionario con los arrays recogidos de una de las tres maneras.
    eventos = list(map(lambda x, y, ts, pol: Event(
        x[0],
        y[0],
        pol[0],
        ts[0]
    )
        #                {
        #     'x': x[0],
        #     'y': y[0],
        #     'ts': ts[0],
        #     'pol': pol[0]
        # }
        , arrays[0], arrays[1], arrays[2], arrays[3]))

    # Devolvemos los eventos calculados
    return eventos


# matlab to abstract
def abstractToMatlab(event_list, output_file):
    print("TODO")
    return