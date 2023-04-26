from ship import SHIP_TYPE_TO_SIZE, Ship


class Board:
    def __init__(self, size: int = 10):
        self.size = size
        self.grid = [['-' for i in range(10)] for j in range(10)]
        self.ships = [Ship(type) for type in SHIP_TYPE_TO_SIZE.keys()]

    def print_board(self, show_ships=False):
        print('   0 1 2 3 4 5 6 7 8 9')
        for i in range(10):
            row = str(i) + '  '
            for j in range(10):
                if show_ships:
                    row += self.grid[i][j] + ' '
                else:
                    if self.grid[i][j] == '-' or self.grid[i][j] in ['X', 'O']:
                        row += self.grid[i][j] + ' '
                    else:
                        row += '- '
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

        if self.grid[x][y] == '-':
            print('Miss!')
            self.grid[x][y] = 'O'
            return

        for ship in self.ships:
            if guess in ship.coords:
                ship.hits.append(guess)
                self.grid[x][y] = 'X'
                print('Hit!')
                if ship.is_sunk():
                    print(f'{ship.name} has been sunk!')
