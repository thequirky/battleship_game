from enum import Enum

from position import Position

SPACE = " "
GAP = 2 * SPACE


class Cell(Enum):
    HIT = "X"
    MISS = "O"
    EMPTY = "-"


class Board:
    def __init__(self, size: int = 10) -> None:
        self.size = size
        self.grid = [[Cell.EMPTY for _ in range(size)] for _ in range(size)]

    def get_value(self, pos: Position) -> Cell:
        return self.grid[pos.x][pos.y]

    def set_value(self, pos: Position, value: Cell) -> None:
        self.grid[pos.x][pos.y] = value

    def is_empty(self, guess: Position) -> bool:
        return self.get_value(guess) == Cell.EMPTY

    def __str__(self) -> str:
        brd_str = GAP + SPACE + SPACE.join(str(idx) for idx in range(self.size))
        for x in range(self.size):
            row = str(x) + GAP
            for y in range(self.size):
                pos = Position(x, y)
                cell_value = self.get_value(pos)
                if cell_value == Cell.EMPTY or cell_value in [Cell.HIT, Cell.MISS]:
                    row += cell_value.value + SPACE
                else:
                    row += Cell.EMPTY.value + SPACE
            brd_str += "\n" + row
        return brd_str


if __name__ == "__main__":
    brd = Board(size=10)
    pos = Position(3, 3)
    brd.set_value(pos, Cell.HIT)
    print(brd)
