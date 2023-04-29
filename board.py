from cell import CellState, Position


BOARD_SIZE = 10

SPACE = " "
GAP = 2 * SPACE


class Board:
    def __init__(self, size: int = BOARD_SIZE):
        self.size = size
        self.grid = [[CellState.EMPTY.value for _ in range(size)] for _ in range(size)]

    def get_value(self, pos: tuple[str, str]) -> str:
        x, y = pos
        return self.grid[x][y]
    
    def set_value(self, pos: tuple[str, str], value: str) -> None:
        x, y = pos
        self.grid[x][y] = value

    def is_empty(self, guess: Position) -> bool:
        return self.get_value(guess) == CellState.EMPTY.value

    def __str__(self):
        brd_str = GAP + SPACE + SPACE.join(str(idx) for idx in range(self.size))
        for i in range(self.size):
            row = str(i) + GAP
            for j in range(self.size):
                if (self.grid[i][j] == CellState.EMPTY.value or 
                    self.grid[i][j] in [CellState.HIT.value, CellState.MISS.value]):
                    row += self.grid[i][j] + SPACE
                else:
                    row += CellState.EMPTY.value + SPACE
            brd_str += "\n" + row
        return brd_str
