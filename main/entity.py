from jsonHandler import JSONFileHandler

file=JSONFileHandler("familyTree.json")



class Entity:
    def __init__(self, arguments):
        data=file.read()
        type=arguments[0]

        if type not in ["relationship","person"]:
            raise Exception("Invalid arguments")
            
        name=" ".join(arguments[1:])
        data[type].append(name)
        file.write(data)
