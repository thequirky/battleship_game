from game import Game
from position import Position, Orientation
from ship import Ship, ShipType
from placement import place_ship_on_position


def main():
    game = Game()
    game.board._reset()
    game.ships = [
        Ship(ShipType.Carrier),
        Ship(ShipType.Cruiser),
        Ship(ShipType.Battleship)
    ]
    place_ship_on_position(
        ship=game.ships[0],
        pos=Position(x=0, y=0),
        board=game.board,
        orientation=Orientation.HORIZONTAL
    )
    place_ship_on_position(
        ship=game.ships[1],
        pos=Position(x=0, y=5),
        board=game.board,
        orientation=Orientation.VERTICAL
    )
    place_ship_on_position(
        game.ships[2],
        pos=Position(x=0, y=6),
        board=game.board,
        orientation=Orientation.HORIZONTAL
    )
    game.board._show_board()
    game.run()


if __name__ == '__main__':
    main()
