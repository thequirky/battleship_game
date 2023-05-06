from enum import Enum


class Cell(Enum):
    HIT = "X"
    MISS = "O"
    EMPTY = "-"

    def __str__(self) -> str:
        return self.value


if __name__ == "__main__":
    cell = Cell.HIT
    print(cell)
