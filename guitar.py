class Guitar:
    def __init__(self):
        self.numStrings : int = 6

    def getNumStrings(self) -> int:
        return self.numStrings

    def play(self):
        print("playing")
