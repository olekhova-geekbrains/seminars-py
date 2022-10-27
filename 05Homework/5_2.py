from random import randint

CNT_CANDY = 2021
CNT_PLAYERS = 2
MAX_CANDY_STEP = 28
MIN_CANDY_STEP = 0

PLAYERS_NAMES = {
    1: 'Player_1',
    2: 'Player_2'
}

def get_first_move_player() -> int:
    """
    ��������� ����� ������, ������� ����� ������ ������
    :return: ����� ������ (1/2)
    """
    return randint(1, CNT_PLAYERS)

def valid_cnt_candy(cnt: int) -> bool:
    """
    �������� ���������� ��������� ������������� ������
    :param cnt: ���������� ������
    :return: True/False
    """

    if MIN_CANDY_STEP <= cnt <= MAX_CANDY_STEP:
        return True
    else:
        return False

def valid_type_value_cnt_candy(cnt: str) -> bool:
    """
    ��������� ������������� �������� - ����� �����?

    :param cnt: ��������� ������������� ��������
    :return: True / False
    """

    if cnt.isdigit():
        return True
    else:
        return False

def valid_value_cnt_candy(cnt: int, full_cnt: int, players_candies: dict) -> bool:
    """
    �� ��������� ��������� ������������� �������� ����������
    ���������� ������
    :param players_candies: ���������� ������ �� ����� � �������
    :param full_cnt: ����� ������
    :param cnt: �������� ������������� ���������� ������
    :return: True/False
    """

    if (full_cnt - (players_candies[1] + players_candies[2])) < cnt:
        return False
    else:
        return True

def get_remainder(players_candies: dict, full_cnt: int) -> int:
    """
    ������� ���������� ���������� ������
    :param players_candies: ���������� ������ �� ����� � �������
    :param full_cnt: ����� ������
    :return: ���������� ���������� ������
    """

    return full_cnt - (players_candies[1] + players_candies[2])

def start_game_human_human():
    """
    ���� � ������ ������� � ���������
    :return: None
    """
    cnt_candy_players: dict = {
        1: 0,
        2: 0
    }

    id_player: int = get_first_move_player()

    while (cnt_candy_players[1] + cnt_candy_players[2]) < CNT_CANDY:
        current_cnt_candy = input(f"{PLAYERS_NAMES[id_player]}, ��� ���: ")

        if not valid_type_value_cnt_candy(current_cnt_candy) or not valid_cnt_candy(int(current_cnt_candy)):
            print(f"���������� ����� ������ [{MIN_CANDY_STEP} , {MAX_CANDY_STEP}]")
            continue

        if not valid_value_cnt_candy(int(current_cnt_candy), CNT_CANDY, cnt_candy_players):
            print(f"{PLAYERS_NAMES[id_player]}, �� �� ������ ����� ������ ������, ��� ��������")
            continue

        cnt_candy_players[id_player] += int(current_cnt_candy)

        print(f"�������� ������: {get_remainder(cnt_candy_players, CNT_CANDY)}")

        id_player = 1 if id_player == 2 else 2

    print(f"������ ������� {PLAYERS_NAMES[1 if id_player == 2 else 2]}")