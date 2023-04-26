from enum import Enum


class CellState(Enum):
    HIDDEN = "H"
    MISSED = "O"
    HIT = "X"


class Position:

    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y


class ShipBuilder:
    ...


class Ship:

    def __init__(self, start: Position, end: Position, damaged: list[Position] = None) -> None:
        self.start = start
        self.end = end
        if damaged is None:
            self._damaged = []

    def do_hit(self, position: Position) -> bool:
        ...

    def is_sunk(self):
        ...


class Board:

    def __init__(self, size: int) -> None:
        self.grid: list[list[str]] = None

    @classmethod
    def from_ship(cls):
        ...

    def place_ship(self):
        ...

    def display(self) -> None:
        ...