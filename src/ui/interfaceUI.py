import abc


class InterfaceUI(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def initialWindow(self, convert, input_file, output_file, input_type, output_type, use_config, config_path):
        """ Shows an initial window for the user """
        pass

    @abc.abstractmethod
    def showMessage(self, message, type_msg="i"):
        """ Shows an message for the user """
        pass

    @abc.abstractmethod
    def sumProgress(self, end=False):
        """ Sum progress to the progress bar """
        pass

    @abc.abstractmethod
    def simpleInput(self, question):
        """ Simple input for the user """
        pass

    @abc.abstractmethod
    def chooseWindow(self, question, options, ret_index=False):
        """ Show a choose selection for the user """
        pass

    @abc.abstractmethod
    def multiInputsWindow(self, question, options):
        """ Show a multi input selection for the user """
        pass

    @abc.abstractmethod
    def errorWindow(self, e):
        """ Shows an error window for the user """
        pass
