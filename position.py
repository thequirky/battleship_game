from collections import namedtuple
from enum import StrEnum, auto


Position = namedtuple("Position", "x y")


class Orientation(StrEnum):
    HORIZONTAL = auto()
    VERTICAL = auto()


if __name__ == "__main__":
    pos = Position(x=2, y=2)
    orientation = Orientation.HORIZONTAL

    print(pos)
    print(orientation)
