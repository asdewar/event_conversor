from src.conversors.mainConverter import convert
from src.utils.utils import choose, checkPathAndType
import src.utils.colors as c

FILE_TYPES = ['txt', 'bag']


def main():

    input_file = input("Introduce the input file name: ")

    input_type = checkPathAndType(input_file, FILE_TYPES)

    output_type = choose("Choose the output type: ", FILE_TYPES)

    output_file = input("Introduce the path of the resultant file: ")

    c.yellow("Starting conversion...")

    convert(input_type, input_file, output_type, output_file)

    c.green("Conversion finished!!!")


if __name__ == '__main__':
    main()
