from src.testing.testUtils import generateRandomFiles, testFileAndType, testTypes, testShuffle
from src.gui.UI import UI


def main():

    UI("graphic")

    generateRandomFiles(10000)

    # testFileAndType("data/matlab/matrix_nx4.mat", "mat")
    # testFileAndType("data/matlab/b_0376.mat", "txt")

    # testTypes("aedat", "aedat")

    # testShuffle(-1)


# Main
if __name__ == '__main__':
    main()
