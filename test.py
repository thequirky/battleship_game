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


class Ship:
    def __init__(self, type: str):
        self.name = type
        self.size = SHIP_TYPE_TO_SIZE[type]
        self.coords = []
        self.hits = []

    def place_ship(self, board):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            orientation = random.choice(list(Orientation))
            if self.check_valid_placement(board, x, y, orientation):
                if orientation == Orientation.HORIZONTAL:
                    for i in range(self.size):
                        board[x][y+i] = self.name[0]
                        self.coords.append((x, y+i))
                else:
                    for i in range(self.size):
                        board[x+i][y] = self.name[0]
                        self.coords.append((x+i, y))
                break

    def check_valid_placement(self, board, x, y, orientation: Orientation):
        if orientation == Orientation.HORIZONTAL:
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
    def __init__(self, size: int = 10):
        self.size = size
        self.board = [['-' for i in range(10)] for j in range(10)]
        self.ships = [Ship(type) for type in SHIP_TYPE_TO_SIZE.keys()]

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
        x, y = guess

        if self.board[x][y] == '-':
            print('Miss!')
            self.board[x][y] = 'O'
            return

        for ship in self.ships:
            if guess in ship.coords:
                ship.hits.append(guess)
                self.board[x][y] = 'X'
                print('Hit!')
                if ship.is_sunk():
                    print(f'{ship.name} has been sunk!')


def main():
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


if __name__ == '__main__':
    main()
