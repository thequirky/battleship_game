from collections import namedtuple
from enum import StrEnum, auto


Position = namedtuple("Position", "x y")


class Orientation(StrEnum):
    HORIZONTAL = auto()
    VERTICAL = auto()