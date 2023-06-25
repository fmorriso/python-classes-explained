from guitar import Guitar


class ElectricGuitar(Guitar):

    def __init__(self):
        super().__init__()
        self.numStrings = 8
        self.color = ("#000000", "#FFFFFF")

    def playLouder(self):
        print("playing".upper())
