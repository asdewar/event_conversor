import struct
from src.format.EventClass import Event
from src.utils.utils import nsecsToSecs, secsToNsecs
import src.utils.constants as cte


def aedat3ToAbstract(input_file):
    f = open(input_file, "rb")

    event_list = []

    # Read comments.
    while True:
        if f.readline().strip() == "#!END-HEADER".encode():
            break

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

    return event_list


def abstractToAedat3(event_list, output_file):
    f = open(output_file, "wb")

    for comment in cte.INITIAL_COMMENTS_AEDAT3:
        f.write(comment.encode())

    # Header
    b = bytearray(28)
    b[20:24] = struct.pack('<I', int(len(event_list)))
    f.write(b)

    # Events
    for e in event_list:
        x = '{0:015b}'.format(e.x)
        y = '{0:015b}'.format(e.y)

        if len(x) != 15 or len(y) != 15:
            raise Exception("In AEDAT 3.1 x and y must be smaller than 32768")

        p = '1' if e.pol else '0'
        address = x + y + p + "0"

        ts = secsToNsecs(e.ts)

        f.write(struct.pack('<I', int(address, 2)))
        # try:
        f.write(struct.pack('<I', int(ts)))
        # except Exception as err:
        #     print("ERROR, TIMESTAMP BIGGER THAN 4 BYTES, CANNOT CONVERT TO AEDAT 3")
        #     raise err

    f.close()
