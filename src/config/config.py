import json
from src.utils.utils import SingletonMeta


class Config(metaclass=SingletonMeta):
    config_data = None
    rosbag = False
    matlab = False
    aedat = False

    def __init__(self, config_path=None):
        if config_path:
            with open(config_path) as f:
                self.config_data = json.load(f)
            if "rosbag" in self.config_data: self.rosbag = True
            if "matlab" in self.config_data: self.matlab = True
            if "aedat" in self.config_data: self.aedat = True
