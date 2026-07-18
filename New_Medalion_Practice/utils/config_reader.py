import json

class ConfigReader:
    @staticmethod
    def read_config(config_path):
        with open(config_path,"r") as f:
            config=json.load(f)
        return config