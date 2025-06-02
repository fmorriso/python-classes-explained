import sys

from electric_guitar import ElectricGuitar
from guitar import Guitar


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def main():
    my_guitar = Guitar()
    print(my_guitar.numStrings)
    print(my_guitar.getNumStrings())
    my_guitar.play()

    my_guitar = ElectricGuitar()
    my_guitar.playLouder()
    print(f'Child class: {my_guitar.numStrings}')
    print(f'Parent class {Guitar().numStrings}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Python version {get_python_version()}')

