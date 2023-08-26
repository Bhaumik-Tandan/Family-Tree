import uuid

class Person:
    def __init__(self, name):
        self.name = name
        self.id = uuid.uuid4()
