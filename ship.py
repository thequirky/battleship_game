from enum import Enum, auto

from board import Board
from cell import CellState as cs, Position


class Orientation(Enum):
    HORIZONTAL = auto()
    VERTICAL = auto()


class ShipType(Enum):
    Carrier = "C"
    Battleship = "B"
    Cruiser = "C"
    Submarine = "S"
    Destroyer = "D"


SHIP_TYPE_TO_SIZE = {
    ShipType.Carrier: 5,
    ShipType.Battleship: 4,
    ShipType.Cruiser: 3,
    ShipType.Submarine: 3,
    ShipType.Destroyer: 2,
}

SHIP_TYPES = list(ShipType)


class Ship:
    def __init__(self, type: str):
        self.type = type
        self.size = SHIP_TYPE_TO_SIZE[type]
        self.coords = []
        self.hits = []

    def place_horizontally(self, pos: Position, board: Board):
        for i in range(self.size):
            new_pos = Position(pos.x, pos.y+i)
            board.set_value(new_pos, self.type.value)
            self.coords.append(new_pos)

    def place_vertically(self, pos: Position, board: Board):
        for i in range(self.size):
            new_pos = Position(pos.x+i, pos.y)
            board.set_value(new_pos, self.type.value)
            self.coords.append(new_pos)

    def can_place_vertically(self, board: Board, pos: Position):
        can_fit = pos.x + self.size < board.size
        if not can_fit:
            return False
        positions = [Position(pos.x, pos.y+i) for i in range(self.size)]
        no_obstacle = all(board.get_value(pos) == cs.EMPTY for pos in positions)
        return no_obstacle
    
    def can_place_horizontally(self, board: Board, pos: Position):
        can_fit = pos.y + self.size < board.size
        if not can_fit:
            return False
        positions = [Position(pos.x+i, pos.y) for i in range(self.size)]
        no_obstacle = all(board.get_value(pos) == cs.EMPTY for pos in positions)
        return no_obstacle

    def can_place(self, board: Board, pos: Position, orientation: Orientation):
        if orientation == Orientation.HORIZONTAL:
            return self.can_place_horizontally(board, pos)
        else:
            return self.can_place_vertically(board, pos)

    def is_sunk(self):
        return len(self.hits) == self.size
