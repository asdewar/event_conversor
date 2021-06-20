from src.utils.utils import nsecsToSecs, secsToNsecs, getNumProgress
from src.format.EventClass import Event
from src.ui.UI import UI
import struct
import os


def binToAbstract(input_file):
    UI().objectUI.showMessage("Starting to read bin file", "w")
    f = open(input_file, "rb")
    event_list = []

    num_progress = getNumProgress(os.path.getsize(input_file) / 5)
    i = 0
    while True:
        if i % num_progress == 0:
            UI().objectUI.sumProgress()
        i += 1

        data = f.read(5)
        if len(data) != 5:
            break
        x = int(data[0])
        y = int(data[1])

        p_ts = int.from_bytes(data[2:], "big")
        p = p_ts >> 23
        ts = p_ts & 8388607

        event_list.append(Event(x, y, p, nsecsToSecs(ts)))

    UI().objectUI.sumProgress(True)
    UI().objectUI.showMessage("Finishing reading the bin file", "c")
    return event_list


def abstractToBin(event_list, output_file):
    UI().objectUI.showMessage("Starting to write bin file", "w")
    f = open(output_file, "wb")

    num_progress = getNumProgress(len(event_list))
    for i, e in enumerate(event_list):
        if i % num_progress == 0:
            UI().objectUI.sumProgress()

        p = '1' if e.pol else '0'
        ts = '{0:023b}'.format(int(secsToNsecs(e.ts)))
        p_ts = p + ts

        # Raises exception if param bigger of what format accepts
        try:
            f.write(struct.pack('<B', e.x))
            f.write(struct.pack('<B', e.y))
            f.write(struct.pack('<B', int(p_ts[:8], 2)))
            f.write(struct.pack('>H', int(p_ts[8:], 2)))
        except Exception:
            raise Exception("Larger parameter than the bin format accepts")

    UI().objectUI.sumProgress(True)
    f.close()
    UI().objectUI.showMessage("Finishing writing the bin file", "c")
