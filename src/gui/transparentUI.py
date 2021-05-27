from src.gui.interfaceUI import InterfaceUI


class TransparentUI(InterfaceUI):

    def initialWindow(self, convert, input_file, output_file, input_type, output_type, use_config, config_path):
        convert(input_file, output_file, input_type, output_type)
        pass

    def showMessage(self, message, type_msg="i"):
        pass

    def sumProgress(self, end=False):
        pass

    def simpleInput(self, question):
        pass

    def chooseWindow(self, question, options, ret_index=False):
        pass

    def multiInputsWindow(self, question, options):
        pass

    def errorWindow(self, e):
        pass
