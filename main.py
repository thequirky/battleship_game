from board import Board


def main():
    guessed_coords = []
    board = Board()
    board.place_all_ships()
    board.print_board(show_ships=True)

    while True:
        guess = board.get_valid_guess(guessed_coords)
        guessed_coords.append(guess)
        board.process_guess(guess)
        board.print_board(show_ships=False)

        if all(ship.is_sunk() for ship in board.ships):
            print('Congratulations! You have sunk all the ships!')
            break


if __name__ == '__main__':
    main()
