import read_book

def name():
    return input('Введите имя: ')


def surname():
    return input('Введите фамилию: ')


def phone():
    while True:
        try:
            int(input('Введите номер телефона: '))
            break
        except ValueError:
            print("Вы ввели не телефон. Попробуйте снова: ")


def comment():
    return input('Введите комментарий: ')





