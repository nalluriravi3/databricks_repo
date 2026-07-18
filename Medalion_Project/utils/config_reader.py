import json

class ConfigReader:

    @staticmethod
    def read_config(config_path):

        with open(config_path, "r") as file:
            return json.load(file)