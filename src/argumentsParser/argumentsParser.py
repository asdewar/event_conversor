from src.utils.utils import getExtension
import src.utils.constants as cte
import argparse


def initialArgs(add_help):
    parser = argparse.ArgumentParser(description='Convert files which contains DVS events', add_help=add_help)

    parser.add_argument('--use_graphic_UI', '-gr', action='store_true',
                        help='Use the graphic user interface (Do not use UI options to run without UI)')
    parser.add_argument('--use_terminal_UI', '-te', action='store_true',
                        help='Use the terminal user interface (Do not use UI options to run without UI)')

    return parser


def parseArguments():
    args = initialArgs(False).parse_known_args()[0]

    required_config = False
    if args.use_graphic_UI:
        opt = "?"
        ui_type = "graphic"
    else:
        opt = 1
        if args.use_terminal_UI:
            ui_type = "terminal"
        else:
            ui_type = "transparent"
            required_config = True

    parser = initialArgs(True)

    # Positionals
    parser.add_argument('input_file', default='', nargs=opt,
                        help='The input file to convert')
    parser.add_argument('output_file', default=cte.OUTPUT_DEFAULT, nargs="?",
                        help='The output file where conversion is created (not put to default output path)')

    # Optionals
    parser.add_argument('--input_type', default='',
                        help='The input type (not introduce to autodetect from input_file)')

    parser.add_argument('--output_type', default='',
                        help='The output type (not introduce to autodetect from output_file)')

    parser.add_argument('--config_path', default=cte.CONFIG_PATH,
                        help='The path of the config file.')

    parser.add_argument('--use_config', action='store_true', required=required_config,
                        help='Put this flag to use the config feature (mandatory in not ui config)')

    args = parser.parse_args()

    if args.input_type == '':
        args.input_type = getExtension(args.input_file)
    if args.output_type == '':
        args.output_type = getExtension(args.output_file)

    if opt == 1:
        args.input_file = args.input_file[0]

    return args.input_file, args.output_file, args.input_type, args.output_type, \
           args.use_config, args.config_path, ui_type
