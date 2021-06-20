from src.utils.utils import nsecsToSecs, secsToNsecs, getNumProgress
from src.format.EventClass import Event
import src.config.constants as cte
from src.ui.UI import UI
import struct

TS_MAX = 2**32


def aedat3ToAbstract(input_file):
    UI().objectUI.showMessage("Starting to read aedat3 file", "w")
    f = open(input_file, "rb")
    event_list = []

    # Read comments.
    while True:
        if f.readline().strip() == "#!END-HEADER".encode():
            break

    UI().objectUI.showMessage("Starting to read the data (no progress bar available)", "w")

    # Read events
    while True:
        headers = f.read(28)
        if len(headers) != 28:
            break
        num_events = int.from_bytes(headers[20:24], "little")
        for _ in range(num_events):
            data = int.from_bytes(f.read(4), "little")
            ts = int.from_bytes(f.read(4), "little")

            x = (data >> 17) & 8191
            y = (data >> 2) & 8191
            p = (data >> 1) & 1

            event_list.append(Event(x, y, p, nsecsToSecs(ts)))

    UI().objectUI.showMessage("Finishing reading the aedat3 file", "c")
    return event_list


def abstractToAedat3(event_list, output_file):
    UI().objectUI.showMessage("Starting to write aedat3 file", "w")
    f = open(output_file, "wb")

    for comment in cte.INITIAL_COMMENTS_AEDAT3:
        f.write(comment.encode())

    # Header
    b = bytearray(28)
    b[20:24] = struct.pack('<I', int(len(event_list)))
    f.write(b)

    # Events
    num_progress = getNumProgress(len(event_list))
    for i, e in enumerate(event_list):
        if i % num_progress == 0:
            UI().objectUI.sumProgress()

        x = '{0:015b}'.format(e.x)
        y = '{0:015b}'.format(e.y)

        if len(x) != 15 or len(y) != 15:
            raise Exception("In aedat3 x and y must be smaller than 32768")

        p = '1' if e.pol else '0'
        address = x + y + p + "0"

        ts = secsToNsecs(e.ts)

        if ts >= TS_MAX:
            raise Exception("Error, timestamp bigger than 4 bytes, cannot convert to aedat3")

        f.write(struct.pack('<I', int(address, 2)))
        f.write(struct.pack('<I', int(ts)))

    UI().objectUI.sumProgress(True)
    f.close()
    UI().objectUI.showMessage("Finishing writing the aedat3 file", "c")
