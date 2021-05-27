from src.utils.utils import secsToNsecs, nsecsToSecs, getNumProgress
from src.format.EventClass import Event
import src.utils.constants as cte
from src.gui.UI import UI
import struct
import os

TS_MAX = 2**32


def aedat2ToAbstract(input_file):
    UI().objectUI.showMessage("Starting to read aedat2 file", "w")

    # Read comments.
    tam_comments = 0
    in_comment = False
    f = open(input_file, "rb")
    while True:
        char = f.read(1)[0]
        if char == 35:
            in_comment = True
        elif char == 10 and in_comment:
            in_comment = False
        elif not in_comment:
            break
        tam_comments += 1

    f.close()

    # Read events
    f = open(input_file, "rb")
    f.read(tam_comments)
    byt = bytearray()
    is_address = True
    event_list = []
    x = 0
    y = 0
    p = 0

    num_progress = getNumProgress(os.path.getsize(input_file) - tam_comments)
    i = 0
    for char in f.read():
        if i % num_progress == 0:
            UI().objectUI.sumProgress()
        i += 1

        byt += bytearray(char.to_bytes(1, 'big'))
        if len(byt) == 4:
            num = struct.unpack('>I', byt)[0]
            byt = bytearray()
            cad = '{0:016b}'.format(num)
            if is_address:
                is_address = False
                y = int(cad[1:8], 2)
                x = int(cad[8:15], 2)
                p = cad[15] == '1'
            else:
                is_address = True
                ts = nsecsToSecs(int(cad, 2))

                event_list.append(Event(x, y, p, ts))

    UI().objectUI.sumProgress(True)
    UI().objectUI.showMessage("Finishing reading the aedat2 file", "c")
    return event_list


def abstractToAedat2(event_list, output_file):
    UI().objectUI.showMessage("Starting to write aedat2 file", "w")
    file = open(output_file, "wb")

    for comment in cte.INITIAL_COMMENTS_AEDAT2:
        file.write(comment.encode())

    num_progress = getNumProgress(len(event_list))
    for i, e in enumerate(event_list):
        if i % num_progress == 0:
            UI().objectUI.sumProgress()

        x = '{0:07b}'.format(e.x)
        y = '{0:07b}'.format(e.y)

        if len(x) != 7 or len(y) != 7:
            raise Exception("In AEDAT 2.0 x and y must be smaller than 128")

        p = '1' if e.pol else '0'
        address = "0" + y + x + p

        ts = secsToNsecs(e.ts)

        if ts >= TS_MAX:
            raise Exception("Error, timestamp bigger than 4 bytes, cannot convert to aedat 2")

        file.write(struct.pack('>I', int(address, 2)))
        file.write(struct.pack('>I', int(ts)))

    UI().objectUI.sumProgress(True)
    file.close()
    UI().objectUI.showMessage("Finishing writing the aedat2 file", "c")
