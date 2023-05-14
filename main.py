from game import Game
from ship import Ship, ShipType


def default_game():
    print("Playing default game.")
    return Game()


def custom_game():
    print("Playing custom game.")
    ships = [
        Ship(ShipType.Carrier),
        Ship(ShipType.Carrier),
        Ship(ShipType.Cruiser),
        Ship(ShipType.Cruiser),
        Ship(ShipType.Battleship),
        Ship(ShipType.Battleship),
    ]
    return Game(ships=ships)


def main(default: bool = True):
    game = default_game() if default else custom_game()
    game.run()


if __name__ == '__main__':
    main()
