from src.gui.interfaceUI import InterfaceUI
from src.gui.graphicUI import GraphicUI
from src.gui.terminalUI import TerminalUI
from src.gui.transparentUI import TransparentUI
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
