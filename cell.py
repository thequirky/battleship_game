from collections import namedtuple
from enum import Enum


Position = namedtuple("Position", "x y")


class CellState(Enum):
    HIT = "X"
    MISS = "O"
    EMPTY = "-"