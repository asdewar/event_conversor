import src.config.constants as cte
import math
import os


def checkPathAndType(path_file, file_type):
    if not os.path.exists(path_file):
        raise Exception("Path {} doesn't exist".format(path_file))

    if file_type not in cte.ADMITTED_TYPES:
        raise Exception("This type of file: ({}) isn't admitted (only {})".format(file_type, cte.ADMITTED_TYPES))


def combine(whole, decimal):
    if decimal == 0:
        return whole
    return whole + (decimal / 1000000000)


def nsecsToSecs(num):
    return num / 1000000000


def secsToNsecs(num):
    return int(num * 1000000000)


def getExtension(file_name):
    if "." in file_name:
        return file_name.split(".")[-1]
    else:
        return ""


def addExtension(path_file, type_file):
    if getExtension(path_file) == "":
        if path_file[-1] == ".":
            return path_file + type_file
        else:
            return path_file + "." + type_file
    else:
        return path_file


def getNumProgress(num_events):
    return math.ceil(num_events / cte.NUM_PROGRESS_BAR)


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]