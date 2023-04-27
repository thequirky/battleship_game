from collections import namedtuple
from enum import Enum, auto
import random


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

Position = namedtuple("Position", "x y")

    
class Ship:
    def __init__(self, type: str):
        self.name = type
        self.size = SHIP_TYPE_TO_SIZE[type]
        self.coords = None
        self.hits = []

    def _place_horizontally(self, pos: Position, board):
        for i in range(self.size):
            board[pos.x][pos.y+i] = self.name[0]
            if self.coords is None:
                self.coords = [(pos.x, pos.y+i)]
            else:
                self.coords.append((pos.x, pos.y+i))

    def place_vertically(self, pos: Position, board):
        for i in range(self.size):
            board[pos.x+i][pos.y] = self.name[0]
            if self.coords is None:
                self.coords = [(pos.x+i, pos.y)]
            self.coords.append((pos.x+i, pos.y))

    def place_ship(self, board):
        while True:
            pos = Position(random.randint(0, 9), random.randint(0, 9))
            orientation = random.choice(list(Orientation))

            if self.is_valid_placement(board, pos, orientation):
                if orientation == Orientation.HORIZONTAL:
                    self.place_horizontally(pos, board)
                else:
                    self.place_vertically(pos, board)
                break

    def is_valid_placement(self, board, pos: Position, orientation: Orientation):
        if orientation == Orientation.HORIZONTAL:
            if pos.y + self.size > 10:
                return False
            for i in range(self.size):
                if board[pos.x][pos.y+i] != '-':
                    return False
        else:
            if pos.x + self.size > 10:
                return False
            for i in range(self.size):
                if board[pos.x+i][pos.y] != '-':
                    return False
        return True

    def is_sunk(self):
        return len(self.hits) == self.size



