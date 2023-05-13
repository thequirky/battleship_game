from __future__ import annotations

from board import Board, Cell
from input import get_valid_guess
from placement import place_ship_randomly
from position import Position
from ship import Ship, SHIP_TYPES


class Game:
    def __init__(self, ships: list[Ship] = None) -> None:
        self.previous_guesses: list[Position] = []
        self.board = Board()
        self.ships = [Ship(type) for type in SHIP_TYPES] if ships is None else ships
        self.place_all_ships()

    def place_all_ships(self) -> None:
        for ship in self.ships:
            place_ship_randomly(ship=ship, board=self.board)

    def process_hit(self, ship: Ship, pos: Position) -> None:
        ship.add_hit(pos)
        self.board.set_value(pos=pos, value=Cell.HIT)

    def process_miss(self, pos: Position) -> None:
        self.board.set_value(pos=pos, value=Cell.MISS)

    def all_sunk(self) -> bool:
        return all(ship.is_sunk() for ship in self.ships)

    def process_guess(self, pos: Position) -> None:
        if self.board.is_empty(pos):
            self.process_miss(pos)
            print("Miss!")
        for ship in self.ships:
            if ship.is_hit(pos):
                self.process_hit(pos=pos, ship=ship)
                print('Hit!')
                if ship.is_sunk():
                    print(f'{ship} has been sunk!')

    def run(self) -> None:
        print(self.board)
        while True:
            guess = get_valid_guess(
                board_size=self.board.size,
                previous_guesses=self.previous_guesses
            )
            self.previous_guesses.append(guess)
            self.process_guess(guess)
            print(self.board)
            if self.all_sunk():
                print('Congratulations! You have sunk all the ships!')
                break
