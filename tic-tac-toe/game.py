import random
import board


def select_player(player1: str, player2: str) -> str:
    first_player = random.choice([player1, player2])
    return first_player


def has_empty_cell(brd: list, sym: str = ' ') -> bool:
    for row in brd:
        if sym in row:
            return True
    return False


def is_empty_cell(brd: list, row, column, sym: str = ' ') -> bool:
    if brd[row][column] == sym:
        return True
    return False


def is_valid_number(data: str) -> bool:
    if data.isdigit() and data in ['1', '2', '3']:
        return True
    return False


def play_ttt(user_x: str, user_o: str) -> str:
    current_player = select_player(user_x, user_o)
    print(f"Первый ходит {current_player}")
    game_progress = [[' ' for _ in range(3)] for _ in range(3)]
    current_board = board.create_board(game_progress)
    print(current_board)
    symbol_x = 'x'
    symbol_o = 'o'
    while True:
        if not has_empty_cell(game_progress): 
            print('Все клетки заполнены.')
            break
        print(f'Ходит игрок {current_player}.')
        while True:
            data = input('Введите номер строки 1, 2 или 3: ')
            if data == '':
                return f'Игрок {current_player} сдался'
            if is_valid_number(data):
                i = int(data) - 1
                break
            else:
                print('Неправильный ввод. Введите еще раз!')
        while True:
            data = input('Введите номер столбца 1, 2 или 3: ')
            if data == '':
                return f'Игрок {current_player} сдался'
            if is_valid_number(data):
                j = int(data) - 1
                break
            else:
                print('Неправильный ввод. Введите еще раз!')
        if is_empty_cell(game_progress, i, j):
            game_progress[i][j] = symbol_x if current_player == user_x else symbol_o
            current_player = user_o if current_player == user_x else user_x
            current_board = board.create_board(game_progress)
        else:
            print('Ячейка занята! Переходите.')
        print(current_board)
    return 'Конец игры'


if __name__ == "__main__":
    name_x = input('Введите имя игрока, который ходит "x": ')
    name_o = input('Введите имя игрока, который ходит "o": ')


    print(play_ttt(name_x, name_o))
