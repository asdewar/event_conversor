import struct

from src.format.EventClass import Event
from src.utils.utils import nsecsToSecs, secsToNsecs


def binToAbstract(input_file):
    event_list = []
    f = open(input_file, "rb")

    while True:
        data = f.read(5)
        if len(data) != 5:
            break
        x = int(data[0])
        y = int(data[1])

        p_ts = int.from_bytes(data[2:], "big")
        p = p_ts >> 23
        ts = p_ts & 8388607

        event_list.append(Event(x, y, p, nsecsToSecs(ts)))

    return event_list


def abstractToBin(event_list, output_file):
    f = open(output_file, "wb")

    for e in event_list:
        p = '1' if e.pol else '0'
        ts = '{0:023b}'.format(int(secsToNsecs(e.ts)))
        p_ts = p + ts

        f.write(struct.pack('<B', e.x))
        f.write(struct.pack('<B', e.y))
        f.write(struct.pack('<B', int(p_ts[:8], 2)))
        try:
            f.write(struct.pack('>H', int(p_ts[8:], 2)))
        except Exception as err:
            print("ERROR, TIMESTAMP BIGGER THAN 23 BITS, CANNOT CONVERT TO BIN")
            raise err

    f.close()
