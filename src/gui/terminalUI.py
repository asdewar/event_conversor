from src.gui.interfaceUI import InterfaceUI
import src.utils.constants as cte
import src.utils.colors as c
import traceback


class TerminalUI(InterfaceUI):
    progress = 0

    def initialWindow(self, convert, input_file, output_file, input_type, output_type, use_config, config_path):
        c.blue("---STARTING CONVERSION---")
        convert(input_file, output_file, input_type, output_type)
        c.blue("---CONVERSION FINISHED---")

    # Must be i(info), w(warning), c(correct)
    def showMessage(self, message, type_msg="i"):
        if type_msg == "i":
            c.white(message)
        elif type_msg == "w":
            c.yellow(message)
        elif type_msg == "c":
            c.green(message)

    def sumProgress(self, end=False):
        if not end:
            c.white("-{}%-".format(self.progress))
            self.progress += cte.NUM_PROGRESS_BAR
        else:
            c.green("-100%-")
            self.progress = 0

    def simpleInput(self, question):
        return input(question)

    def chooseWindow(self, question, options, ret_index=False):
        c.blue(question)
        for i, option in enumerate(options):
            c.white("[{}] {}".format(i, option))
        try:
            index = int(input("Introduce the INDEX of the element: "))
            return index if ret_index else list(options)[index]
        except ValueError:
            raise Exception('The input must be an integer')
        except IndexError:
            raise Exception('Option out of bounds')

    def multiInputsWindow(self, question, options):
        c.blue(question)
        ret_list = []

        c.white("Write the NAME for each option:")
        for option in options:
            ret_list.append(input("{}: ".format(option)))

        return ret_list

    def errorWindow(self, e):
        c.red("AN ERROR OCCURRED: " + str(e))
        traceback.print_exc()
