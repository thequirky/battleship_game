import random

from board import Board, Cell
from ship import Orientation, Position, Ship, SHIP_TYPES


def place_ship_on_position(ship: Ship, pos: Position, board: Board, orientation: Orientation) -> None:
    if orientation == Orientation.HORIZONTAL:
        positions = [Position(pos.x, pos.y + i) for i in range(ship.size)]
    else:
        positions = [Position(pos.x + i, pos.y) for i in range(ship.size)]
    for p in positions:
        board.set_value(p, ship.type.value)
        ship.coords.append(p)

def can_place_ship_on_position(ship: Ship, board: Board, pos: Position, orientation: Orientation) -> bool:
    can_fit_vertically = pos.x + ship.size < board.size
    can_fit_horizontally = pos.y + ship.size < board.size
    if orientation == Orientation.VERTICAL and can_fit_vertically:
        positions = [Position(pos.x + i, pos.y) for i in range(ship.size)]
    elif orientation == Orientation.HORIZONTAL and can_fit_horizontally:
        positions = [Position(pos.x, pos.y + i) for i in range(ship.size)]
    else:
        return False
    has_no_obstacles = all(board.get_value(pos) == Cell.EMPTY for pos in positions)
    return has_no_obstacles

def place_ship_randomly(ship: Ship, board: Board) -> None:
    while True:
        pos = Position(random.randint(0, board.size - 1), random.randint(0, board.size - 1))
        orientation = random.choice(list(Orientation))
        if can_place_ship_on_position(ship=ship, board=board, pos=pos, orientation=orientation):
            place_ship_on_position(ship=ship, pos=pos, board=board, orientation=orientation)
            break


class Game:
    def __init__(self) -> None:
        self.already_guessed: list[Position] = []
        self.board = Board()
        self.ships = [Ship(type) for type in SHIP_TYPES]
        self.place_all_ships()

    def place_all_ships(self) -> None:
        for ship in self.ships:
            place_ship_randomly(ship=ship, board=self.board)

    def get_valid_guess(self) -> Position:
        while True:
            x = input('Enter your row guess: ')
            y = input('Enter your column guess: ')
            x, y = int(x), int(y)
            guess = Position(x, y)
            if guess in self.already_guessed:
                print('You already guessed that, try again')
            elif x > self.board.size - 1 or y > self.board.size - 1:
                print('Invalid guess, try again')
            else:
                return guess

    def process_guess(self, guess) -> str:
        if self.board.is_empty(guess):
            self.board.set_value(guess, Cell.MISS)
            return "Miss!"
        for ship in self.ships:
            if guess in ship.coords:
                ship.hits.append(guess)
                self.board.set_value(guess, Cell.HIT)
                msg = 'Hit!\n'
                if ship.is_sunk():
                    msg += f'{ship.type.name} has been sunk!'
        return msg

    def run(self) -> None:
        print(self.board)
        while True:
            guess = self.get_valid_guess()
            self.already_guessed.append(guess)
            print(self.process_guess(guess))
            print(self.board)
            if all(ship.is_sunk() for ship in self.ships):
                print('Congratulations! You have sunk all the ships!')
                break


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
