import os
import yaml
from configparser import ConfigParser

INI_FILE = os.path.join(os.getcwd(), "config", "inter_api.ini")
YAML_FILE = os.path.join(os.getcwd(), 'config', 'test.yaml')

class ReadIni:
    def __init__(self) -> None:
        self.cf = ConfigParser()
        self.cf.read(INI_FILE, encoding="utf-8")

    def get_value(self, sec, opt) -> str:
        value = self.cf.get(sec, opt)
        return value

    def get_int_value(self, sec, opt) -> int:
        value = self.cf.getint(sec, opt)
        return value

    def get_boolean_value(self, sec, opt) -> bool:
        value = self.cf.getboolean(sec, opt)
        return value

def read_yaml():
    with open(YAML_FILE, 'r', encoding="UTF-8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data