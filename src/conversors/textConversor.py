from src.formatFiles.EventClass import Event


def textToAbstract(input_file):
    events = open(input_file).readlines()
    events_list = []
    for event in events:
        data = event.strip('\n').split(' ')
        events_list.append(Event(
            int(data[1]),         # Integer
            int(data[2]),         # Integer
            int(data[3]) == 1,  # Boolean
            float(data[0])       # Double
        ))

    return events_list


def abstractToText(event_list, output_file):
    f = open(output_file, "w")

    for event in event_list:
        f.write("{:.9f} {} {} {}\n".format(
            event.ts,
            event.x,
            event.y,
            int(event.pol),
        ))
    f.close()
