from testing.src.testUtils import testGenerateRandomEvents, testSaveEventsByType, testLoadEventsByFile, equalEventList


def main():
    event_list = testGenerateRandomEvents()

    print("Checking bag write and reading")
    testSaveEventsByType(event_list, "bag")
    event_list_bag = testLoadEventsByFile("bag")
    equalEventList(event_list, event_list_bag)

    print("Checking txt write and reading")
    testSaveEventsByType(event_list, "txt")
    event_list_txt = testLoadEventsByFile("txt")
    equalEventList(event_list, event_list_txt)

    print("Checking bag and txt compatibility")
    equalEventList(event_list_bag, event_list_txt)


# Main de python
if __name__ == '__main__':
    main()
