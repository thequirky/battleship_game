from enum import Enum, auto

from board import Board, Position, Cell


class Orientation(Enum):
    HORIZONTAL = auto()
    VERTICAL = auto()


class ShipType(Enum):
    Carrier = auto()
    Battleship = auto()
    Cruiser = auto()
    Submarine = auto()
    Destroyer = auto()


SHIP_TYPE_TO_SIZE = {
    ShipType.Carrier: 5,
    ShipType.Battleship: 4,
    ShipType.Cruiser: 3,
    ShipType.Submarine: 3,
    ShipType.Destroyer: 2,
}

SHIP_TYPES = SHIP_TYPE_TO_SIZE.keys()


class Ship:
    def __init__(self, type: Enum):
        self.type = type
        self.size = SHIP_TYPE_TO_SIZE[type]
        self.coords: list[Position] = []
        self.hits: list[Position] = []

    def place_horizontally(self, pos: Position, board: Board):
        positions = [Position(pos.x, pos.y + i) for i in range(self.size)]
        for p in positions:
            board.set_value(p, self.type.value)
            self.coords.append(p)

    def place_vertically(self, pos: Position, board: Board) -> bool:
        positions = [Position(pos.x + i, pos.y) for i in range(self.size)]
        for p in positions:
            board.set_value(p, self.type.value)
            self.coords.append(p)

    def can_place_vertically(self, board: Board, pos: Position) -> bool:
        can_fit = pos.x + self.size < board.size
        if not can_fit:
            return False
        positions = [Position(pos.x + i, pos.y) for i in range(self.size)]
        no_obstacle = all(board.get_value(pos) == Cell.EMPTY for pos in positions)
        return no_obstacle

    def can_place_horizontally(self, board: Board, pos: Position) -> bool:
        can_fit = pos.y + self.size < board.size
        if not can_fit:
            return False
        positions = [Position(pos.x, pos.y + i) for i in range(self.size)]
        no_obstacle = all(board.get_value(pos) == Cell.EMPTY for pos in positions)
        return no_obstacle

    def can_place(self, board: Board, pos: Position, orientation: Orientation) -> bool:
        if orientation == Orientation.HORIZONTAL:
            return self.can_place_horizontally(board, pos)
        else:
            return self.can_place_vertically(board, pos)

    def is_sunk(self):
        return len(self.hits) == self.size

    def __repr__(self):
        return f"Ship(type={self.type}, size={self.size}, coords={self.coords}, hits={self.hits})"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    ship = Ship(ShipType.Battleship)
    print(ship)
