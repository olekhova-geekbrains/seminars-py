def show_main_menu():
    while True:
        data = input('''
        ==============================
        Выберете действие:
        1 - создать запись
        2 - извлечь запись по ID
        3 - обновить запись по ID
        4 - удалить запись по ID
        5 - импорт из CSV файла с ID
        6 - импорт из CSV файла без ID
        7 - сделать выборку по фамилии
        8 - сделать выборку по классу
        9 - закончить работу
        ''')
        if data == '': break
        if not data in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('Неправильный ввод. Введите еще раз!')
        else:
            return int(data)


def show_surname():
    return input('Введите фамилию: ')


def show_name():
    return input('Введите имя: ')


def show_group():
    return input('Введите класс: ')


def show_id():
    return input('Введите id: ')


def show_filename():
    return input('Введите имя файла ')


def show_record(record: dict):
    print('------------------')
    for key, value in record.items():
        print(f'{key}: {value}')


def show_no_record():
    print('Такой записи нет!')


def show_message_new_record():
    print('Введите новые данные.')


def show_message_delete_record():
    print('Запись была удалена.')


def show_message_update():
    print('Данные обновились.')