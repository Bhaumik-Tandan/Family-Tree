import sys
sys.path.append('main')
from entity import Entity

from familyTree import FamilyTree
def main():
    arguments = sys.argv[1:]

    if not arguments:
        raise Exception("No command provided")
        return

    if arguments[0] == "add":
        Entity(arguments[1:])

    elif arguments[0] == "connect":
        FamilyTree.connectPeople(arguments[1:])

    elif arguments[0] == "count":
        FamilyTree.countPeople(arguments[1:])

    else:
        raise Exception("Invalid command")
        
    


if __name__ == "__main__":
    main()
