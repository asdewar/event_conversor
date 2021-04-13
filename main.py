import rosbag

from src.conversors.mainConverter import convert
from src.conversors.rosbagConversor import abstractToRosbag, rosbagToAbstract

# x -> int
# y -> int
# pol -> bool
# ts -> float

in_file = "data/rosbag/shapes_rotation.bag"

out_file = "output/output.bag"

ll = [
        {
            "x": 1,
            "y": 2,
            "pol": True,
            "ts": 1233.99879
        },
        {
            "x": 3,
            "y": 4,
            "pol": False,
            "ts": 987311.112133
        },
        {
            "x": 5,
            "y": 5,
            "pol": True,
            "ts": 76443.41231
        }
    ]


def main():

    print("inicio")

    # # Parseo de argumentos.
    # parser = argparse.ArgumentParser(description='A program that converts rosbag to abstract')

    # # Path del archivo a convertir.
    # parser.add_argument('--path', '-p', help='path of the file to convert')

    # # Parseamos los argumentos con el parser.
    # args = parser.parse_args()

    # # TODO: path para debug
    # path = './datasets/rosbag/rosbag_example/boxes.bag'

    # convert("data/txt/small.txt", "txt", "data/rosbag/small2.bag", "bag")

    convert("data/rosbag/small2.bag", "bag", "output/output.txt", "txt")


# Main de python
if __name__ == '__main__':
    main()
