import random
import PySimpleGUI as sg
import os.path
from src.conversors.mainConverter import getEventsFromFile, putEventsInFile
from src.utils import colors as c
from src.testing.testUtils import testGenerateRandomEvents, equalEventList, getListOfFiles
import src.utils.constants as cte


def main():

    file_list_column = [
        [
            sg.Text("Image Folder"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
            )
        ],
    ]

    image_viewer_column = [
        [sg.Text("Choose an image from list on left:")],
        [sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.Image(key="-IMAGE-")],
    ]

    layout = [
        [
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(image_viewer_column),
        ]
    ]

    window = sg.Window("Image Viewer", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                # Get list of files in folder
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                   and f.lower().endswith((".png", ".gif"))
            ]
            window["-FILE LIST-"].update(fnames)

        elif event == "-FILE LIST-":  # A file was chosen from the listbox
            try:
                filename = os.path.join(
                    values["-FOLDER-"], values["-FILE LIST-"][0]
                )
                window["-TOUT-"].update(filename)
                window["-IMAGE-"].update(filename=filename)
            except:
                pass

    window.close()




    # Config(True)
    # testFileAndType("data/txt/events.txt", "bin")

    # testFileAndType("data/matlab/b_0376.mat", "txt")


    # testTypes("mat", "mat")

    # testShuffle(5)

    # event_list_aedat = getEventsFromFile("data/aedat/aedat2/cards_1.aedat")
    #
    # putEventsInFile(event_list_aedat, "pedro.aedat")
    #
    # event_list_aedat4 = getEventsFromFile("pedro.aedat")
    #
    # equalEventList(event_list_aedat, event_list_aedat4)
    # print("CASI FIN")
    # print(len(event_list_aedat))
    # print(len(event_list_aedat4))

    # event_list_aedat = testLoadEventsByFile("aedat", "data/aedat/aedat4/Cars_sequence.aedat4")
    #
    # testSaveEventsByType(event_list_aedat, "aedat", "pedro.aedat")
    #
    # event_list_aedat4 = testLoadEventsByFile("aedat", "pedro.aedat")
    #
    # equalEventList(event_list_aedat, event_list_aedat4)
    # print("CASI FIN")
    # print(len(event_list_aedat))
    # print(len(event_list_aedat4))


def testShuffle(cutoff):
    all_data_files = getListOfFiles(cte.DATA_PATH)
    random.shuffle(all_data_files)

    for file in all_data_files:
        try:
            type_convert = random.choice(cte.ADMITTED_TYPES)
            testFileAndType(file, type_convert)
            print("Everything OKKKKKKKKK")
        except Exception as err:
            print(err)
            print("FAAAAAAAAAAIIIIIIIIIILLLLLLLLLL")


def testFileAndType(file_name_1, type_convert):
    c.blue("Testing\n\tfile: {}\n\ttype: {}".format(file_name_1, type_convert))
    file_name_2 = cte.OUTPUT_DEFAULT + type_convert
    event_list_1 = getEventsFromFile(file_name_1)
    putEventsInFile(event_list_1, file_name_2)
    event_list_2 = getEventsFromFile(file_name_2)
    equalEventList(event_list_1, event_list_2)


def testTypes(type1, type2):
    event_list_random = testGenerateRandomEvents(200)
    file1 = cte.OUTPUT_DEFAULT + type1
    file2 = cte.OUTPUT_DEFAULT + type2

    putEventsInFile(event_list_random, file1)
    event_list_1 = getEventsFromFile(file1)
    putEventsInFile(event_list_1, file2)
    event_list_2 = getEventsFromFile(file2)

    equalEventList(event_list_random, event_list_1)
    equalEventList(event_list_random, event_list_2)


# Main
if __name__ == '__main__':
    main()
