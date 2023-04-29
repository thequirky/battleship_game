from enum import Enum, auto

from board import Board
from cell import Position


class Orientation(Enum):
    HORIZONTAL = auto()
    VERTICAL = auto()


SHIP_TYPE_TO_SIZE = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2,
}

SHIP_TYPES = SHIP_TYPE_TO_SIZE.keys()


class Ship:
    def __init__(self, type: str):
        self.name = type
        self.size = SHIP_TYPE_TO_SIZE[type]
        self.coords = []
        self.hits = []

    def place_horizontally(self, pos: Position, board):
        for i in range(self.size):
            board.grid[pos.x][pos.y+i] = self.name[0]
            self.coords.append((pos.x, pos.y+i))

    def place_vertically(self, pos: Position, board):
        for i in range(self.size):
            board.grid[pos.x+i][pos.y] = self.name[0]
            self.coords.append((pos.x+i, pos.y))

    def is_valid_placement(self, board: Board, pos: Position, orientation: Orientation):
        if orientation == Orientation.HORIZONTAL:
            if pos.y + self.size > 10:
                return False
            for i in range(self.size):
                if board.grid[pos.x][pos.y+i] != '-':
                    return False
        else:
            if pos.x + self.size > 10:
                return False
            for i in range(self.size):
                if board.grid[pos.x+i][pos.y] != '-':
                    return False
        return True

    def is_sunk(self):
        return len(self.hits) == self.size
