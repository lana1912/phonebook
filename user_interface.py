
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


def format():
    return input('Выберите формат записи 1 - строку, 2 - в столбик: ')


def conclusion():
      return input('Выберите формат вывода 1 - в строку, 2 - в столбик: ')
