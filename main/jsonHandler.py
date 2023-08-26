import json

class JSONFileHandler:
    _instance = None

    def __new__(cls, filename):
        if JSONFileHandler._instance is None:
            JSONFileHandler._instance = super().__new__(cls)
            JSONFileHandler._instance.filename = filename
        return JSONFileHandler._instance


    def read(self):
        with open(self.filename, "r") as file:
            data = json.load(file)
        return data

    def write(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file)
