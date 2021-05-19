import json
import src.utils.constants as cte


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Config(metaclass=SingletonMeta):
    config_data = None
    rosbag = False
    matlab = False
    aedat = False

    def __init__(self, use_config=False):
        if use_config:
            with open(cte.CONFIG_PATH) as f:
                self.config_data = json.load(f)
            if "rosbag" in self.config_data: self.rosbag = True
            if "matlab" in self.config_data: self.matlab = True
            if "aedat" in self.config_data: self.aedat = True
