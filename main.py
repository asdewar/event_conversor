from src.argumentsParser.argumentsParser import parseArguments
from src.converters.mainConverter import convert
from src.config.config import Config
from src.gui.UI import UI

FILE_TYPES = ['txt', 'bag']


def main():
    # Args parse.
    input_file, output_file, input_type, output_type, use_config, config_path, ui_type = parseArguments()

    # Init config features.
    if use_config:
        Config(config_path)

    # Create UI.
    if ui_type == "graphic":
        UI("graphic")
    elif ui_type == "terminal":
        UI("terminal")

    # Init UI.
    try:
        UI().objectUI.initialWindow(convert, input_file, output_file, input_type, output_type, use_config, config_path)
    except Exception as e:
        UI().objectUI.errorWindow(e)


if __name__ == '__main__':
    main()
