class FamilyTree:
    _instance = None

    def __new__(cls):
        if FamilyTree._instance is None:
            FamilyTree._instance = super().__new__(cls)
        return FamilyTree._instance