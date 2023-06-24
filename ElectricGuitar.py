from guitar import Guitar


class ElectricGuitar(Guitar):

    def __init__(self):
        super().__init__()

    def playLouder(self):
        print("playing".upper())
