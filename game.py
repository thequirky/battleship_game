from board import Board


class Game:
    def __init__(self) -> None:
        self.guessed_coords = []
        self.board = Board()

    def run(self):

        self.board.place_all_ships()
        self.board.print_board(show_ships=True)

        while True:
            guess = self.board.get_valid_guess(self.guessed_coords)
            self.guessed_coords.append(guess)
            self.board.process_guess(guess)
            self.board.print_board(show_ships=False)

            if all(ship.is_sunk() for ship in self.board.ships):
                print('Congratulations! You have sunk all the ships!')
                break
