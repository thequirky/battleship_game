from board import Board
from game import Game
from position import Position
from ship import Ship


def main():
    from ship import ShipType
    from placement import place_ship_on_position
    from position import Orientation

    game = Game()
    game.board = Board()
    game.ships = [Ship(ShipType.Carrier), Ship(ShipType.Cruiser), Ship(ShipType.Battleship)]
    place_ship_on_position(game.ships[0], Position(x=0, y=0), game.board, orientation=Orientation.HORIZONTAL)
    place_ship_on_position(game.ships[1], Position(x=0, y=5), game.board, orientation=Orientation.VERTICAL)
    place_ship_on_position(game.ships[2], Position(x=0, y=6), game.board, orientation=Orientation.HORIZONTAL)
    for row in range(game.board.size):
        print(game.board.grid[row])
    game.run()


if __name__ == '__main__':
    main()
