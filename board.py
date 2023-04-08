from enum import Enum


class Cell(Enum):
    HIDDEN = "H"
    MISS = "O"
    HIT = "X"


class Ship:
    ...


class Board:

    def __init__(self, size: int) -> None:
        self.grid: list[list[str]] = None

    @classmethod
    def from_ship(cls):
        ...
