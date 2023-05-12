from position import Position


def get_number(prompt: str) -> int:
    while True:
        value = input(prompt)
        try:
            value = int(value)
            return value
        except ValueError:
            print("Not a number, try again")


def get_valid_guess(board_size: int, previous_guesses: list[Position]) -> Position:
    while True:
        x = get_number('Enter your row guess: ')
        y = get_number('Enter your column guess: ')
        guess = Position(x, y)
        if already_guessed(guess=guess, previous_guesses=previous_guesses):
            print('You already guessed that, try again')
        elif not is_inside(pos=guess, board_size=board_size):
            print('Guess not inside the board, try again')
        else:
            return guess


def already_guessed(guess: Position, previous_guesses: list[Position]) -> bool:
    return guess in previous_guesses


def is_inside(pos: Position, board_size: int) -> bool:
    return pos.x < board_size and pos.y < board_size
