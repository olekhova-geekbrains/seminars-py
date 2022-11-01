from colorama import Fore, Style
import random
import board
from colorama import init
init(autoreset=True)


EMPTY_SYMBOL = ' '


def select_player(player1: str, player2: str) -> str:
    first_player = random.choice([player1, player2])
    return first_player


def has_empty_cell(game_pr: list, sym: str = EMPTY_SYMBOL) -> bool:
    for el in game_pr:
        if el == sym:
            return True
    return False


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
            print(Fore.RED + 'Неправильный ввод. Введите еще раз!')
    return num


def get_victory_line(game_pr: list, sym: str = EMPTY_SYMBOL) -> list:
    row1 = [game_pr[0], game_pr[1], game_pr[2]]
    row2 = [game_pr[3], game_pr[4], game_pr[5]]
    row3 = [game_pr[6], game_pr[7], game_pr[8]]
    column1 = [game_pr[0], game_pr[3], game_pr[6]]
    column2 = [game_pr[1], game_pr[4], game_pr[7]]
    column3 = [game_pr[2], game_pr[5], game_pr[8]]
    diag1 = [game_pr[0], game_pr[4], game_pr[8]]
    diag2 = [game_pr[2], game_pr[4], game_pr[6]]
    if row1[0] != sym and len(set(row1)) == 1:
        print(Fore.GREEN + 'Первая строка выиграла')
        return [0,1,2]
    if row2[0] != sym and len(set(row2)) == 1:
        print(Fore.GREEN + 'Вторая строка выиграла')
        return [3, 4, 5]
    if row3[0] != sym and len(set(row3)) == 1:
        print(Fore.GREEN + 'Третья строка выиграла')
        return [6, 7, 8]
    if column1[0] != sym and len(set(column1)) == 1:
        print(Fore.GREEN + 'Первый столбец выиграл')
        return [0, 3, 6]
    if column2[0] != sym and len(set(column2)) == 1:
        print(Fore.GREEN + 'Второй столбец выиграл')
        return [1, 4, 7]
    if column3[0] != sym and len(set(column3)) == 1:
        print(Fore.GREEN + 'Третий столбец выиграл')
        return [2, 5, 8]
    if diag1[0] != sym and len(set(diag1)) == 1:
        print(Fore.GREEN + 'Главная диагональ выиграла')
        return [0, 4, 8]
    if diag2[0] != sym and len(set(diag2)) == 1:
        print(Fore.GREEN + 'Побочная диагональ выиграла')
        return [2, 4, 6]
    return None


def colorize_element(game_pr: list, vct_line: list) -> list:
    for el in vct_line:
        game_pr[el] = Fore.GREEN + game_pr[el] + Style.RESET_ALL
    return game_pr


def play_ttt(user_x: str, user_o: str, sym: str = EMPTY_SYMBOL) -> str:
    current_player = select_player(user_x, user_o)
    print(f"Первый ходит {current_player}")

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
            game_progress[idx] = symbol_x if current_player == user_x else symbol_o
            current_board = board.create_board(game_progress)
            victory_line = get_victory_line(game_progress)
            if victory_line:
                game_progress = colorize_element(game_progress, victory_line)
                current_board = board.create_board(game_progress)
                print(current_board)
                return f'Игрок {current_player} выиграл!'
            current_player = user_o if current_player == user_x else user_x
        else:
            print(Fore.RED + 'Ячейка занята! Переходите.')

        print(current_board)
    return 'Конец игры. Ничья.'


if __name__ == "__main__":
    name_x = input('Введите имя игрока, который ходит "x": ')
    name_o = input('Введите имя игрока, который ходит "o": ')

    print(play_ttt(name_x, name_o))
