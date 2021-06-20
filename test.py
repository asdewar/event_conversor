from src.config.config import Config
from src.testing.testUtils import generateRandomFiles, testFileAndType, testTypes, testShuffle
from src.ui.UI import UI


def main():

    UI("terminal")

    Config("src/config/config.json")

    # testFileAndType("data/aedat/aedat4/Cars_sequence.aedat4", "aedat")

    testTypes("aedat", "aedat")


# Main
if __name__ == '__main__':
    main()
