from src.format.EventClass import Event
import aedat

from src.utils.utils import nsecsToSecs


def aedat4ToAbstract(input_file):
    decoder = aedat.Decoder(input_file)
    event_list = []

    for packet in decoder:
        if 'events' in packet:
            for ev in packet['events']:
                event_list.append(Event(
                    ev[1],
                    ev[2],
                    ev[3],
                    nsecsToSecs(ev[0])
                ))

    return event_list


def abstractToAedat4(event_list, output_file):

    pass
