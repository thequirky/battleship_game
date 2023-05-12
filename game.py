from __future__ import annotations

from board import Board, Cell
from input import get_valid_guess
from placement import place_ship_randomly
from position import Position
from ship import Ship, SHIP_TYPES


class Game:
    def __init__(self, ships: list[Ship] = None) -> None:
        self.already_guessed: list[Position] = []
        self.board = Board()
        self.ships = [Ship(type) for type in SHIP_TYPES] if ships is None else ships
        self.place_all_ships()

    def place_all_ships(self) -> None:
        for ship in self.ships:
            place_ship_randomly(ship=ship, board=self.board)

    def process_guess(self, guess) -> str:
        if self.board.is_empty(guess):
            self.board.set_value(guess, Cell.MISS)
            return "Miss!"
        for ship in self.ships:
            if ship.is_hit(guess):
                ship.add_hit(guess)
                self.board.set_value(guess, Cell.HIT)
                msg = 'Hit!\n'
                if ship.is_sunk():
                    msg += f'{ship.type.name} has been sunk!'
        return msg

    def run(self) -> None:
        print(self.board)
        while True:
            guess = get_valid_guess(
                board_size=self.board.size,
                already_guessed=self.already_guessed
            )
            self.already_guessed.append(guess)
            print(self.process_guess(guess))
            print(self.board)
            all_sunk = all(ship.is_sunk() for ship in self.ships)
            if all_sunk:
                print('Congratulations! You have sunk all the ships!')
                break


def main():
    game = Game()
    game.run()

    # from ship import ShipType
    #
    # ships = [
    #     Ship(ShipType.Carrier),
    #     Ship(ShipType.Cruiser),
    #     Ship(ShipType.Battleship),
    # ]
    # game = Game(ships=ships)
    # game.run()


if __name__ == '__main__':
    main()
