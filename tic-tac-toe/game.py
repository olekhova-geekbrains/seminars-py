from colorama import Fore, Style
import random
import board
from colorama import init
init(autoreset=True)


def select_player(player1: str, player2: str) -> str:
    first_player = random.choice([player1, player2])
    return first_player


def has_empty_cell(game_pr: list) -> bool:
    for el in game_pr:
        if not el:
            return True
    return False


def is_empty_cell(game_pr: list, idx: int) -> bool:
    if game_pr[idx]:
        return False
    return True


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


def get_victory_line(game_pr: list) -> list:
    line_idx = (
        ((0, 1, 2),"Первая строка"),
        ((3, 4, 5),"Вторая строка"),
        ((6, 7, 8), "Третья строка"),
        ((0, 3, 6), "Первый столбец"),
        ((1, 4, 7), "Второй столбец"),
        ((2, 5, 8), "Третий столбец"),
        ((0, 4, 8), "Главная диагональ"),
        ((2, 4, 6), "Побочная диагональ"))
    for (li, name) in line_idx:
        line = [game_pr[i] for i in li]
        if line[0] and len(set(line)) == 1:
            print(Fore.GREEN + f'{name}')
            return li
    return None


def colorize_element(game_pr: list, vct_line: list) -> list:
    for el in vct_line:
        game_pr[el] = Fore.GREEN + game_pr[el] + Style.RESET_ALL
    return game_pr


def play_ttt(user_x: str, user_o: str) -> str:
    current_player = select_player(user_x, user_o)
    print(f"Первый ходит {current_player}")

    game_progress = [None for _ in range(9)]
    current_board = board.create_board(game_progress)
    print(current_board)

    symbol_x = 'x'
    symbol_o = 'o'
    while True:
        if not has_empty_cell(game_progress):
            print('Все клетки заполнены.')
            break
        print(f'Ходит игрок {current_player}.')

        phrases = ['Введите номер строки 1, 2 или 3: ',
                   'Введите номер стобца 1, 2 или 3: ']
        cell = []
        for i in range(2):
            i = enter_number(phrases[i])
            if i == -1:
                return f'Игрок {current_player} сдался.'
            cell.append(i)

        idx = cell[0] * 3 + cell[1]

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
