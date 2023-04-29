BOARD_SIZE = 10

HIT = "X"
MISS = "O"
EMPTY = "-"

SPACE = " "
GAP = 2 * SPACE


class Board:
    def __init__(self, size: int = BOARD_SIZE):
        self.size = size
        self.grid = [[EMPTY for _ in range(size)] for _ in range(size)]

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
    
    def set_value(self, pos: tuple[str, str], value: str) -> None:
        x, y = pos
        self.grid[x][y] = value

    def is_empty(self, guess) -> bool:
        return self.get_value(guess) == EMPTY

    def __str__(self):
        brd_str = GAP + SPACE + SPACE.join(str(idx) for idx in range(self.size))
        for i in range(self.size):
            row = str(i) + GAP
            for j in range(self.size):
                if self.grid[i][j] == EMPTY or self.grid[i][j] in [HIT, MISS]:
                    row += self.grid[i][j] + SPACE
                else:
                    row += EMPTY + SPACE
            brd_str += "\n" + row
        return brd_str
