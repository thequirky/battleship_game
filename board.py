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
        self.grid = self.reset()

    def reset(self) -> list[Cell]:
        return [[Cell.EMPTY for _ in range(self.size)] for _ in range(self.size)]

    def get_value(self, pos: Position) -> Cell:
        return self.grid[pos.x][pos.y]

    def set_value(self, pos: Position, value: Cell) -> None:
        self.grid[pos.x][pos.y] = value

    def is_empty(self, guess: Position) -> bool:
        return self.get_value(guess) == Cell.EMPTY

    def __str__(self) -> str:
        brd_str = GAP + SPACE.join(str(idx) for idx in range(self.size))
        for row_nb, row in enumerate(self.grid):
            row_str = str(row_nb) + SPACE
            for cell in row:
                row_str += cell.value if cell in [Cell.HIT, Cell.MISS] else Cell.EMPTY.value + SPACE
            brd_str += "\n" + row_str
        return brd_str

    def _show_board(self) -> None:
        for row in self.grid:
            row_items = [
                cell[0].upper() if isinstance(cell, str) else cell.name[0] for cell in row
            ]
            print(" ".join(row_items))
        print('\n')


if __name__ == "__main__":
    brd = Board()
    brd.set_value(pos=Position(x=4, y=2), value=Cell.HIT)
    brd.set_value(pos=Position(x=6, y=9), value=Cell.MISS)
    print(brd)
