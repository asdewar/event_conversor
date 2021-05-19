import struct
from src.format.EventClass import Event
from src.utils.utils import secsToNsecs, nsecsToSecs
import src.utils.constants as cte


def aedat2ToAbstract(input_file):
    f = open(input_file, "rb")

    byt = bytearray()
    in_comment = True
    is_address = True
    event_list = []
    comment_section = True

    for char in f.read():
        # Comments control
        if char == 35 and comment_section:
            in_comment = True
        elif char == 10 and in_comment and comment_section:
            in_comment = False
        # Data control
        elif not in_comment:
            comment_section = False
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

    return event_list


def abstractToAedat2(event_list, output_file):
    file = open(output_file, "wb")

    for comment in cte.INITIAL_COMMENTS_AEDAT2:
        file.write(comment.encode())

    for e in event_list:
        x = '{0:07b}'.format(e.x)
        y = '{0:07b}'.format(e.y)

        if len(x) != 7 or len(y) != 7:
            raise Exception("In AEDAT 2.0 x and y must be smaller than 128")

        p = '1' if e.pol else '0'
        address = "0" + y + x + p

        ts = secsToNsecs(e.ts)

        file.write(struct.pack('>I', int(address, 2)))
        try:
            file.write(struct.pack('>I', int(ts)))
        except Exception as err:
            print("ERROR, TIMESTAMP BIGGER THAN 4 BYTES, CANNOT CONVERT TO AEDAT 2")
            raise err

    file.close()
