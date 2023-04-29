from collections import namedtuple
from enum import Enum


Position = namedtuple("Position", "x y")


class CellState(Enum):
    HIT = "X"
    MISS = "O"
    EMPTY = "-"

    def __str__(self) -> str:
        return self.value


if __name__ == "__main__":
    cell = CellState.HIT
    print(cell)
    pos = Position(x=1, y=0)
    print(pos)
