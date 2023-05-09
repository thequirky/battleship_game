from position import Position


def get_number(prompt: str) -> int:
    while True:
        value = input(prompt)
        try:
            value = int(value)
            return value
        except ValueError:
            print("Not a number, try again")


def get_valid_guess(board_size: int, already_guessed: list[Position]) -> Position:
    while True:
        x = get_number('Enter your row guess: ')
        y = get_number('Enter your column guess: ')
        guess = Position(x, y)
        if guess in already_guessed:
            print('You already guessed that, try again')
        elif x > board_size - 1 or y > board_size - 1:
            print('Invalid guess, try again')
        else:
            return guess
