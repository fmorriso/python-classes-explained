import sys

from ElectricGuitar import ElectricGuitar
from guitar import Guitar


@staticmethod
def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Python versioun {get_python_version()}')
    my_guitar = Guitar()
    print(my_guitar.numStrings)
    print(my_guitar.getNumStrings())

    my_guitar = ElectricGuitar()
    my_guitar.playLouder()
