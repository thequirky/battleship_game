import random
from board import HIT, MISS, Board
from ship import Orientation, Position, Ship, SHIP_TYPES


class Game:
    def __init__(self) -> None:
        self.guessed_coords = []
        self.board = Board()
        self.ships = [Ship(type) for type in SHIP_TYPES]
        self.place_all_ships()

    def place_all_ships(self):
        for ship in self.ships:
            self.place_ship(ship)

    def place_ship(self, ship: Ship):
        while True:
            pos = Position(random.randint(0, 9), random.randint(0, 9))
            orientation = random.choice(list(Orientation))

            if ship.is_valid_placement(self.board, pos, orientation):
                if orientation == Orientation.HORIZONTAL:
                    ship.place_horizontally(pos, self.board)
                else:
                    ship.place_vertically(pos, self.board)
                break

    def process_guess(self, guess) -> str:
        if self.board.is_empty(guess):
            self.board.set_value(guess, MISS)
            return "Miss!"

        for ship in self.ships:
            if guess in ship.coords:
                ship.hits.append(guess)
                self.board.set_value(guess, HIT)
                msg = 'Hit!\n'
                if ship.is_sunk():
                    msg += f'{ship.name} has been sunk!'
        return msg

    def run(self) -> None:

        print(self.board)

        while True:
            guess = self.board.get_valid_guess(self.guessed_coords)
            self.guessed_coords.append(guess)
            print(self.process_guess(guess))
            print(self.board)

            if all(ship.is_sunk() for ship in self.ships):
                print('Congratulations! You have sunk all the ships!')
                break
