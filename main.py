
from game import Game
from ship import Ship


def default_game():
    print("Playing default game.")
    return Game()


def custom_game_example():
    print("Playing custom game.")

    from ship import ShipType
    
    ships = [
        Ship(ShipType.Carrier),
        Ship(ShipType.Cruiser),
        Ship(ShipType.Battleship),
    ]
    return Game(ships=ships)


def main(default: bool = True):
    game = default_game() if default else custom_game_example()
    game.run()


if __name__ == '__main__':
    main()
