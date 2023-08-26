import uuid
from jsonHandler import JSONFileHandler

file=JSONFileHandler("familyTree.json")



class Entity:
    def __init__(self, arguments):
        data=file.read()
        type=arguments[0]

        if type not in ["relationship","person"]:
            raise Exception("Invalid arguments")

        id = str(uuid.uuid4())
        name=" ".join(arguments[1:])
        data[type].append({"id":id,"name":name})
        file.write(data)
