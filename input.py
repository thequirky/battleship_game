from position import Position


def get_valid_guess(board_size: int, already_guessed: list[Position]) -> Position:
    while True:
        x = input('Enter your row guess: ')
        y = input('Enter your column guess: ')
        x, y = int(x), int(y)
        guess = Position(x, y)
        if guess in already_guessed:
            print('You already guessed that, try again')
        elif x > board_size - 1 or y > board_size - 1:
            print('Invalid guess, try again')
        else:
            return guess
