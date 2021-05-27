from src.format.EventClass import Event
from src.utils.utils import nsecsToSecs
from src.gui.UI import UI
import aedat


def aedat4ToAbstract(input_file):
    UI().objectUI.showMessage("Starting to read aedat4 file", "w")
    decoder = aedat.Decoder(input_file)
    event_list = []

    UI().objectUI.showMessage("Starting to read the data (no progress bar available)", "w")
    for packet in decoder:
        if 'events' in packet:
            for ev in packet['events']:
                event_list.append(Event(
                    ev[1],
                    ev[2],
                    ev[3],
                    nsecsToSecs(ev[0])
                ))

    UI().objectUI.showMessage("Finishing reading the aedat4 file", "c")
    return event_list


def abstractToAedat4(event_list, output_file):
    UI().objectUI.showMessage("Starting to write aedat4 file", "w")


    pass


    UI().objectUI.showMessage("Finishing writing the aedat4 file", "c")
