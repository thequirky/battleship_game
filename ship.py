from enum import StrEnum, auto

from position import Position


class ShipType(StrEnum):
    Carrier = auto()
    Battleship = auto()
    Cruiser = auto()
    Submarine = auto()
    Destroyer = auto()


SHIP_TYPE_TO_SIZE = {
    ShipType.Carrier: 5,
    ShipType.Battleship: 4,
    ShipType.Cruiser: 3,
    ShipType.Submarine: 3,
    ShipType.Destroyer: 2,
}

SHIP_TYPES = SHIP_TYPE_TO_SIZE.keys()


class Ship:
    def __init__(self, type: StrEnum):
        self.type = type
        self.size = SHIP_TYPE_TO_SIZE[type]
        self.coords: list[Position] = []
        self.hits: list[Position] = []

    def is_sunk(self) -> bool:
        return len(self.hits) == self.size

    def is_hit(self, pos: Position) -> bool:
        return pos in self.coords

    def add_hit(self, pos: Position) -> None:
        if not self.is_hit:
            raise ValueError(f"Could not hit ship, ship not in position {pos.x}, {pos.y}")
        self.hits.append(pos)

    def __repr__(self) -> str:
        return f"Ship(type={self.type}, size={self.size}, coords={self.coords}, hits={self.hits})"

    def __str__(self) -> str:
        return self.__repr__()


if __name__ == "__main__":
    ship = Ship(ShipType.Battleship)
    print(ship)
