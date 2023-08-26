from entity import Entity
import sys
def main():
    arguments = sys.argv[1:]

    if not arguments:
        print("Invalid command")
        return

    if arguments[0] == "add":
        Entity(arguments[1:])

    


if __name__ == "__main__":
    main()
