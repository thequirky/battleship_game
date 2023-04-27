from ship import SHIP_TYPE_TO_SIZE, Ship


HIT = "X"
MISS = "O"
EMPTY = "-"

SHIP_TYPES = SHIP_TYPE_TO_SIZE.keys()


class Board:
    def __init__(self, size: int = 10):
        self.size = size
        self.grid = [['-' for i in range(size)] for j in range(size)]
        self.ships = [Ship(type) for type in SHIP_TYPES]

    def print_board(self, show_ships=False):
        print('   0 1 2 3 4 5 6 7 8 9')
        for i in range(self.size):
            row = str(i) + '  '
            for j in range(self.size):
                if show_ships:
                    row += self.grid[i][j] + ' '
                    continue
                if self.grid[i][j] == EMPTY or self.grid[i][j] in [HIT, MISS]:
                    row += self.grid[i][j] + ' '
                else:
                    row += EMPTY + " "
            print(row)

    def place_all_ships(self):
        for ship in self.ships:
            ship.place_ship(self.grid)

    def get_valid_guess(self, guessed_coords):
        while True:
            guess = input('Enter your guess (row, column): ')
            guess = guess.split(',')
            guess = (int(guess[0]), int(guess[1]))
            if guess in guessed_coords:
                print('You already guessed that, try again')
            elif guess[0] not in range(10) or guess[1] not in range(10):
                print('Invalid guess, try again')
            else:
                return guess

    def process_guess(self, guess):
        x, y = guess

        if self.grid[x][y] == EMPTY:
            print('Miss!')
            self.grid[x][y] = MISS
            return

        for ship in self.ships:
            if guess in ship.coords:
                ship.hits.append(guess)
                self.grid[x][y] = HIT
                print('Hit!')
                if ship.is_sunk():
                    print(f'{ship.name} has been sunk!')
