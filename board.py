BOARD_SIZE = 10

HIT = "X"
MISS = "O"
EMPTY = "-"

SPACE = " "
GAP = 2 * SPACE


class Board:
    def __init__(self, size: int = BOARD_SIZE):
        self.size = size
        self.grid = [[cs.EMPTY for _ in range(size)] for _ in range(size)]

    def get_valid_guess(self, guessed_coords: list):
        while True:
            guess = input('Enter your guess (row, column): ')
            guess = guess.split(',')
            guess = (int(guess[0]), int(guess[1]))
            if guess in guessed_coords:
                print('You already guessed that, try again')
            elif guess[0] not in range(BOARD_SIZE) or guess[1] not in range(BOARD_SIZE):
                print('Invalid guess, try again')
            else:
                return guess

    def get_value(self, pos: tuple[str, str]) -> str:
        x, y = pos
        return self.grid[x][y]
    
    def set_value(self, pos: Position, value: str) -> None:
        self.grid[pos.x][pos.y] = value

    def is_empty(self, guess: Position) -> bool:
        return self.get_value(guess) == cs.EMPTY

    def __str__(self):
        brd_str = GAP + SPACE + SPACE.join(str(idx) for idx in range(self.size))
        for x in range(self.size):
            row = str(x) + GAP
            for y in range(self.size):
                pos = Position(x,y)
                cell_value = self.get_value(pos)
                row += str(cell_value) + SPACE
            brd_str += "\n" + row
        return brd_str


    # def __str__(self):
    #     brd_str = GAP + SPACE + SPACE.join(str(idx) for idx in range(self.size))
    #     for x in range(self.size):
    #         row = str(x) + GAP
    #         for y in range(self.size):
    #             pos = Position(x,y)
    #             cell_value = self.get_value(pos)
    #             if (cell_value == cs.EMPTY or 
    #                 cell_value in [cs.HIT, cs.MISS]):
    #                 row += str(cell_value) + SPACE
    #             else:
    #                 row += str(cs.EMPTY) + SPACE
    #         brd_str += "\n" + row
    #     return brd_str

if __name__ == "__main__":
    brd = Board(size=8)
    print(brd)
    pos = Position(3,3)
    brd.set_value(pos, cs.HIT)
    print(brd)
