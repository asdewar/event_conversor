import matlab_ev


def main():

    eventos_comun = {
        'x': [2, 7, 10, 20, 30, 5, 23, 65],
        'y': [23, 54, 2, 8, 56, 98, 12, 12],
        'p': [1, 0, 1, 0, 1, 0, 0, 0],
        'ts': [759653183, 759653184, 759653185, 759653186, 759653187, 759653188, 759653189, 759653190]
    }

    matlab_ev.comun_a_matlab(eventos_comun, 'prueba1.mat')


if __name__ == '__main__':
    main()
