import random

class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.coords = []
        self.hits = []

    def place_ship(self, board):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            orientation = random.choice(['horizontal', 'vertical'])
            if self.check_valid_placement(board, x, y, orientation):
                if orientation == 'horizontal':
                    for i in range(self.size):
                        board[x][y+i] = self.name[0]
                        self.coords.append((x, y+i))
                else:
                    for i in range(self.size):
                        board[x+i][y] = self.name[0]
                        self.coords.append((x+i, y))
                break

    def check_valid_placement(self, board, x, y, orientation):
        if orientation == 'horizontal':
            if y + self.size > 10:
                return False
            for i in range(self.size):
                if board[x][y+i] != '-':
                    return False
        else:
            if x + self.size > 10:
                return False
            for i in range(self.size):
                if board[x+i][y] != '-':
                    return False
        return True

    def is_sunk(self):
        return len(self.hits) == self.size

class Board:
    def __init__(self):
        self.board = [['-' for i in range(10)] for j in range(10)]
        self.ships = []
        self.create_ships()

    def create_ships(self):
        self.ships.append(Ship('Carrier', 5))
        self.ships.append(Ship('Battleship', 4))
        self.ships.append(Ship('Cruiser', 3))
        self.ships.append(Ship('Submarine', 3))
        self.ships.append(Ship('Destroyer', 2))

    def print_board(self, show_ships=False):
        print('   0 1 2 3 4 5 6 7 8 9')
        for i in range(10):
            row = str(i) + '  '
            for j in range(10):
                if show_ships:
                    row += self.board[i][j] + ' '
                else:
                    if self.board[i][j] == '-' or self.board[i][j] in ['X', 'O']:
                        row += self.board[i][j] + ' '
                    else:
                        row += '- '
            print(row)

    def place_all_ships(self):
        for ship in self.ships:
            ship.place_ship(self.board)

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
        row, col = guess
        if self.board[row][col] != '-':
            for ship in self.ships:
                if guess in ship.coords:
                    ship.hits.append(guess)
                    self.board[row][col] = 'X'
                    print('Hit!')
                    if ship.is_sunk():
                        print(f'{ship.name} has been sunk!')
        else:
            print('Miss!')
            self.board[row][col] = 'O'


if __name__ == '__main__':
    board = Board()
    board.place_all_ships()
    board.print_board(show_ships=False)

    guessed_coords = []
    while True:
        guess = board.get_valid_guess(guessed_coords)
        guessed_coords.append(guess)
        board.process_guess(guess)
        board.print_board(show_ships=False)

        if all(ship.is_sunk() for ship in board.ships):
            print('Congratulations! You have sunk all the ships!')
            break
