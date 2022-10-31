import random
import board

EMPTY_SYMBOL = ' '


def select_player(player1: str, player2: str) -> str:
    first_player = random.choice([player1, player2])
    return first_player


# def has_empty_cell(brd: list, sym: str = ' ') -> bool:
#     for row in brd:
#         if sym in row:
#             return True
#     return False
def has_empty_cell(game_pr: list, sym: str = EMPTY_SYMBOL) -> bool:
    for el in game_pr:
        if el == sym:
            return True
    return False


# def is_empty_cell(brd: list, row, column, sym: str = ' ') -> bool:
#     if brd[row][column] == sym:
#         return True
#     return False
def is_empty_cell(game_pr: list, idx: int, sym: str = EMPTY_SYMBOL) -> bool:
    if game_pr[idx] == sym:
        return True
    return False


def is_valid_number(data: str) -> bool:
    if data.isdigit() and data in ['1', '2', '3']:
        return True
    return False


def enter_number(phrase: str) -> int:
    while True:
        data = input(phrase)
        if data == '':
            return -1
        if is_valid_number(data):
            num = int(data) - 1
            break
        else:
            print('Неправильный ввод. Введите еще раз!')
    return num


def is_victory(game_pr: list, sym: str = EMPTY_SYMBOL) -> bool:
    row1 = [game_pr[0], game_pr[1], game_pr[2]]
    row2 = [game_pr[3], game_pr[4], game_pr[5]]
    row3 = [game_pr[6], game_pr[7], game_pr[8]]
    column1 = [game_pr[0], game_pr[3], game_pr[6]]
    column2 = [game_pr[0], game_pr[3], game_pr[6]]
    column3 = [game_pr[0], game_pr[3], game_pr[6]]
    diag1 = [game_pr[0], game_pr[5], game_pr[8]]
    diag2 = [game_pr[2], game_pr[5], game_pr[6]]
    if row1[0] != sym and len(set(row1)) == 1:
        print('Первая строка выиграла')
        return True
    if row2[0] != sym and len(set(row2)) == 1:
        print('Вторая строка выиграла')
        return True
    if row3[0] != sym and len(set(row3)) == 1:
        print('Третья строка выиграла')
        return True
    if column1[0] != sym and len(set(column1)) == 1:
        print('Первый столбец выиграл')
        return True
    if column2[0] != sym and len(set(column2)) == 1:
        print('Второй столбец выиграл')
        return True
    if column3[0] != sym and len(set(column3)) == 1:
        print('Третий столбец выиграл')
        return True
    if diag1[0] != sym and len(set(diag1)) == 1:
        print('Главная диагонали выиграла')
        return True
    if diag2[0] != sym and len(set(diag2)) == 1:
        print('Побочная диагональ выиграла')
        return True
    return False


def play_ttt(user_x: str, user_o: str, sym: str = EMPTY_SYMBOL) -> str:
    current_player = select_player(user_x, user_o)
    print(f"Первый ходит {current_player}")

    # game_progress = [[' ' for _ in range(3)] for _ in range(3)]
    game_progress = [sym for _ in range(9)]
    current_board = board.create_board(game_progress)
    print(current_board)

    symbol_x = 'x'
    symbol_o = 'o'
    while True:
        if not has_empty_cell(game_progress):
            print('Все клетки заполнены.')
            break
        print(f'Ходит игрок {current_player}.')

        i = enter_number('Введите номер строки 1, 2 или 3: ')
        if i == -1:
            return f'Игрок {current_player} сдался.'

        j = enter_number('Введите номер стобца 1, 2 или 3: ')
        if j == -1:
            return f'Игрок {current_player} сдался.'

        idx = i * 3 + j
        if is_empty_cell(game_progress, idx):
        # if is_empty_cell(game_progress, i, j):
            game_progress[idx] = symbol_x if current_player == user_x else symbol_o
            # game_progress[i][j] = symbol_x if current_player == user_x else symbol_o
            current_board = board.create_board(game_progress)
            if is_victory(game_progress):
                print(current_board)
                return f'Игрок {current_player} выиграл!'
            current_player = user_o if current_player == user_x else user_x
        else:
            print('Ячейка занята! Переходите.')

        print(current_board)
    return 'Конец игры. Ничья.'


if __name__ == "__main__":
    name_x = input('Введите имя игрока, который ходит "x": ')
    name_o = input('Введите имя игрока, который ходит "o": ')

    print(play_ttt(name_x, name_o))
