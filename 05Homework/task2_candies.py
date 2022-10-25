# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит некоторое кол-во конфет, например 220. 
# Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота b) Подумайте как наделить бота "интеллектом"
#     Подумайте об алгоритме игры. Здесь есть ключевые числа количества конфет, 
# которые точно определят победу.

from random import randint, choice


def select_game() -> int:
    while True:
        data = input('''Выберете номер игры:
                1 - Играют двое игроков
                2 - Игрок играет против бота
                3 - Игрок играет против умного бота
        ''')
        if data == "":
            break
        if not data in ['1','2','3']:
            print('Неправильный ввод. Введите еще раз!')
        else:
            num_game = int(data)
            return num_game
    return None


def select_player(player1: str, player2: str) -> str:
    first_player = choice([player1, player2])
    return first_player


def move_player(cur_heap: int, max_candies: int) -> int:
    taken_candies = int(input('Сколько конфет Вы возьмете? '))
    if taken_candies > max_candies or taken_candies <= 0 or taken_candies > cur_heap:
        print('Столько конфет взять нельзя. Переходите!')
        move_player(cur_heap, max_candies)
    return taken_candies


def move_bot(cur_heap: int, max_candies: int) -> int:
    taken_candies = randint(1, min(max_candies, cur_heap))
    return taken_candies


def move_clever_bot(cur_heap: int, max_candies: int) -> int:
    taken_candies = cur_heap % (max_candies + 1)
    if taken_candies == 0:
        taken_candies = max_candies
    return taken_candies


def play_candy(user1: str, user2: str, count: int, max_candies: int) -> str:
    heap = count
    current_player = select_player(user1, user2)
    print(f"Первый ходит {current_player}")
    while heap > 0:
        print(f'Ходит {current_player}, осталось конфет: {heap}')
        if current_player == 'bot':
            taken_candies = move_bot(heap, max_candies)
        elif current_player == 'clever_bot':
            taken_candies = move_clever_bot(heap, max_candies)
        else:
            taken_candies = move_player(heap, max_candies)
        print(f'Игрок {current_player} взял {taken_candies} конфет')
        heap -= taken_candies
        if heap == 0:
            break
        current_player = user2 if current_player == user1 else user1
    return current_player

if __name__ == "__main__":
    count_candies = int(input('Сколько всего конфет? '))
    max_candies = int(input('Максимальное число конфет, которое можно взять: '))
    number_game = select_game()
    name1 = input('Введите имя игрока: ')
    if number_game == 1:
        name2 = input('Введите имя игрока: ')
    elif number_game == 2:
        name2 = 'bot'
    else:
        name2 = 'clever_bot'
    print(f"Победитель: {play_candy(name1, name2, count_candies, max_candies)}")
