import random
import board


def generate_game_progress() -> list:
    result = [[random.choice(['o', 'x', ' ']) for _ in range(3)] for _ in range(3)]
    return result


game_progress = generate_game_progress()
print(game_progress)
progress_board = board.create_board(game_progress)
print(progress_board)
