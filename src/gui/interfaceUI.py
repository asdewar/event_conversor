import abc


class InterfaceUI(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def initialWindow(self, convert, input_file, output_file, input_type, output_type, use_config, config_path):
        """ Shows an initial window for the user """
        pass

    @abc.abstractmethod
    def showMessage(self, message, type_msg="i"):
        """ Shows an initial window for the user """
        pass

    @abc.abstractmethod
    def sumProgress(self, end=False):
        pass

    @abc.abstractmethod
    def simpleInput(self, question):
        pass

    @abc.abstractmethod
    def chooseWindow(self, question, options, ret_index=False):
        """ Shows an initial window for the user """
        pass

    @abc.abstractmethod
    def multiInputsWindow(self, question, options):
        """ Shows an initial window for the user """
        pass

    @abc.abstractmethod
    def errorWindow(self, e):
        """ Shows an initial window for the user """
        pass
