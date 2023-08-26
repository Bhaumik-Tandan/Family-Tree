from jsonHandler import JSONFileHandler

file=JSONFileHandler("familyTree.json")
class FamilyTree:
    def __init__(self):
        raise Exception("Cannot instantiate this class")

    def connectPeople(arguments):
        # Example input: ["Amit", "Dhakad", "as", "son", "of", "KK", "Dhakad"]

        # Find the index of the "as" keyword
        as_index = arguments.index("as")

        # Extract the names of the first person
        relatedTo= " ".join(arguments[:as_index])

        # Extract the relationship keyword
        relationship = arguments[as_index + 1]

        # Extract the names of the second person
        relative= " ".join(arguments[as_index + 3:])

        data=file.read()

        if relationship not in data["relationship"]:
            raise Exception("Invalid relationship")

        if relatedTo not in data["person"]:
            raise Exception("Invalid person")

        if relative not in data["person"]:
            raise Exception("Invalid person")

        data["relationships"].append({
            "relatedTo": relatedTo,
            "relationship": relationship,
            "relative": relative
        })

        file.write(data)











    