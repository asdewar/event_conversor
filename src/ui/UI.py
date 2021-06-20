from src.ui.interfaceUI import InterfaceUI
from src.ui.graphicUI import GraphicUI
from src.ui.terminalUI import TerminalUI
from src.ui.transparentUI import TransparentUI
from src.utils.utils import SingletonMeta


class UI(metaclass=SingletonMeta):

    objectUI: InterfaceUI = None

    def __init__(self, type_ui=None):
        if type_ui == "graphic":
            self.objectUI = GraphicUI()
        elif type_ui == "terminal":
            self.objectUI = TerminalUI()
        else:
            self.objectUI = TransparentUI()
