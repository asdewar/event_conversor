from src.utils.utils import getExtension
from src.ui.interfaceUI import InterfaceUI
from src.config.config import Config
import src.config.constants as cte
import PySimpleGUI as sg
import traceback
import os

font_family = "Helvetica"
font_size = 13
grey_green = "#5D7570"
white_green = "#C3F7EA"
dark_green = "#397567"
fluorescent_green = "#77F5D8"
normal_green = "#5FC2AB"
light_red = "#ffb5b7"


class GraphicUI(InterfaceUI):
    progress = 0
    window = None

    def initialWindow(self, convert, input_file="", output_file=cte.OUTPUT_DEFAULT, input_type="", output_type="",
                      use_config=False, config_path=cte.CONFIG_PATH):

        input_type_aux = input_type if input_type != "" else getExtension(input_file)
        output_type_aux = output_type if output_type != "" else getExtension(output_file)

        input_layout = [
            [
                sg.Text("Input path", size=(12, 1), text_color="white", background_color=grey_green),
                sg.In(size=(35, 1), key="INPUT FILE", enable_events=True, default_text=input_file),
                sg.FileBrowse()
            ],
            [
                sg.Text("Detected input type", size=(12, 1), text_color="white", background_color=grey_green),
                sg.Combo(cte.ADMITTED_TYPES, key="INPUT TYPE", default_value=input_type_aux, size=(10, 1))
            ]
        ]
        output_layout = [
            [
                sg.Text("Output path", size=(12, 1), text_color="white", background_color=grey_green),
                sg.In(size=(35, 1), key="OUTPUT FILE", enable_events=True, default_text=output_file),
                sg.FileBrowse()
            ],
            [
                sg.Text("Output type", size=(12, 1), text_color="white", background_color=grey_green),
                sg.Combo(cte.ADMITTED_TYPES, key="OUTPUT TYPE", default_value=output_type_aux, size=(10, 1),
                         enable_events=True)
            ]
        ]

        config_layout = [
            [
                sg.Text("Config file path", size=(12, 1), text_color="white", background_color=grey_green),
                sg.In(size=(35, 1), key="CONFIG PATH", enable_events=True, default_text=config_path),
                sg.FileBrowse(),
            ],
            [
                sg.Radio('Use config file', 'CONFIG RADIO', key="USE CONFIG", default=use_config,
                         background_color=grey_green),
                sg.Radio('Do not use config file', 'CONFIG RADIO', key="NOT USE CONFIG", default=not use_config,
                         background_color=grey_green)
            ]
        ]

        buttons_layout = [
            [
                sg.Button("RESET"),
                sg.Button("CONVERT")
            ]
        ]

        layout = [
            [
                input_layout,
                [[sg.HSeparator()]],
                output_layout,
                [[sg.HSeparator()]],
                config_layout,
                [[sg.HSeparator()]],
                buttons_layout
            ]
        ]

        self.window = sg.Window("Event Converter", layout, size=(1000, 500), margins=(30, 35), resizable=True,
                                font=(font_family, font_size), background_color=grey_green, button_color=dark_green)

        while True:
            event, values = self.window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break

            elif event == "RESET":
                self.window.Element('INPUT FILE').Update(value="")
                self.window.Element('INPUT TYPE').Update(value="")
                self.window.Element('OUTPUT FILE').Update(value="")
                self.window.Element('OUTPUT TYPE').Update(value="")
                self.window.Element('CONFIG PATH').Update(value="")
                self.window.Element('NOT USE CONFIG').Update(value=True)

            elif event == "INPUT FILE":
                ext = getExtension(values["INPUT FILE"])
                if ext in cte.ADMITTED_TYPES:
                    self.window.Element('INPUT TYPE').Update(value=ext)

            elif event == "OUTPUT FILE":
                ext = getExtension(values["OUTPUT FILE"])
                if ext in cte.ADMITTED_TYPES:
                    self.window.Element('OUTPUT TYPE').Update(value=ext)

            elif event == "OUTPUT TYPE":
                ext = values["OUTPUT TYPE"]
                file = values["OUTPUT FILE"]
                tam = len(getExtension(file))
                if tam > 0:
                    file = file[:-tam]
                if file[-1] == ".":
                    file += ext
                else:
                    file += "." + ext
                self.window.Element('OUTPUT FILE').Update(value=file)

            elif event == "CONVERT":
                i_f = values["INPUT FILE"]
                i_t = values["INPUT TYPE"]
                o_f = values["OUTPUT FILE"]
                o_t = values["OUTPUT TYPE"]
                u_c = values["USE CONFIG"]
                c_p = values["CONFIG PATH"]

                if not os.path.isfile(i_f):
                    sg.popup_error("The input file does not exists")
                elif u_c and not os.path.isfile(c_p):
                    sg.popup_error("The config file does not exists")
                elif i_t not in cte.ADMITTED_TYPES:
                    sg.popup_error("The input type is not supported")
                elif o_t not in cte.ADMITTED_TYPES:
                    sg.popup_error("The output type is not supported")
                else:
                    if u_c:
                        Config(c_p)
                    convert(i_f, o_f, i_t, o_t)
                    sg.popup('CONVERSION FINISHED!!!')

        self.window.close()

    def showMessage(self, message, type_msg="i"):
        if type_msg == "i":
            sg.popup(message)
        elif type_msg == "w":
            sg.popup(message, button_color=("black", "yellow"))
        elif type_msg == "c":
            sg.popup(message, button_color=("black", "green"))

    def sumProgress(self, end=False):
        canceled = False
        if not end:
            canceled = not sg.one_line_progress_meter('Progress bar', self.progress, cte.NUM_PROGRESS_BAR, 'PROGRESS BAR',
                                                      'Converting progress bar', orientation='h',
                                                      bar_color=(dark_green, "white"), button_color=dark_green)
            self.progress += 1
        else:
            sg.one_line_progress_meter('Progress bar', 100, 100, 'PROGRESS BAR', 'Converting progress bar',
                                       orientation='h', bar_color=(dark_green, "white"), button_color=dark_green)
            self.progress = 0
        if canceled:
            if sg.popup_yes_no('Cancel conversion?') == "Yes":
                exit()

    def simpleInput(self, question):
        return sg.popup_get_text(question)

    def chooseWindow(self, question, options, ret_index=False):
        cad = question + '\n'
        for i, option in enumerate(options):
            cad += ("[{}] {}\n".format(i, option))
        cad += "Introduce the INDEX of the element: "
        try:
            index = int(sg.popup_get_text(cad))
            return index if ret_index else list(options)[index]
        except ValueError:
            raise Exception('The input must be an integer')
        except IndexError:
            raise Exception('Option out of bounds')

    def multiInputsWindow(self, question, options):
        cad = question + '\n'
        ret_list = []

        cad += "Write the NAME for each option:\n"
        for option in options:
            ret_list.append(sg.popup_get_text(cad + "{}:\n".format(option)))

        return ret_list

    def errorWindow(self, e):
        tb = traceback.format_exc()
        if sg.popup_yes_no('An error occurred:\n' + str(e) + '\nShow traceback?', text_color=light_red) == "Yes":
            sg.popup_error('EXCEPTION:', e, tb)
