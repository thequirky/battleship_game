import random
from board import BOARD_SIZE, Board
from cell import CellState as cs, Position
from ship import Orientation, Ship, SHIP_TYPES


class Game:
    def __init__(self) -> None:
        self.guessed_coords : list [Position] = []
        self.board = Board()
        self.ships = [Ship(type) for type in SHIP_TYPES]
        self.place_all_ships()

    def place_all_ships(self) -> None:
        for ship in self.ships:
            self.place_ship(ship)

    def place_ship(self, ship: Ship) -> None:
        while True:
            pos = Position(random.randint(0, 9), random.randint(0, 9))
            orientation = random.choice(list(Orientation))

            if ship.can_place(self.board, pos, orientation):
                if orientation == Orientation.HORIZONTAL:
                    ship.place_horizontally(pos, self.board)
                else:
                    ship.place_vertically(pos, self.board)
                break

    def get_valid_guess(self) -> Position:
        while True:
            guess = input('Enter your guess (row, column): ')
            guess = guess.split(',')
            guess = Position(int(guess[0]), int(guess[1]))
            if guess in self.guessed_coords:
                print('You already guessed that, try again')
            elif guess[0] not in range(BOARD_SIZE) or guess[1] not in range(BOARD_SIZE):
                print('Invalid guess, try again')
            else:
                return guess

    def process_guess(self, guess) -> str:
        if self.board.is_empty(guess):
            self.board.set_value(guess, cs.MISS.value)
            return "Miss!"

        for ship in self.ships:
            if guess in ship.coords:
                ship.hits.append(guess)
                self.board.set_value(guess, cs.HIT.value)
                msg = 'Hit!\n'
                if ship.is_sunk():
                    msg += f'{ship.type.name} has been sunk!'
        return msg

    def run(self) -> None:

        print(self.board)

        while True:
            guess = self.get_valid_guess()
            self.guessed_coords.append(guess)
            print(self.process_guess(guess))
            print(self.board)

            if all(ship.is_sunk() for ship in self.ships):
                print('Congratulations! You have sunk all the ships!')
                break
