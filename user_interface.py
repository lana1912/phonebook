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

def console_line(data: tuple):
    print(f'Имя: {data[0]} Фамилия: {data[1]} Телефон: {data[2]} Комментарий: {data[3]}')

def console_colunm(data: tuple):
    print(f'Имя: {data[0]}\n Фамилия: {data[1]}\n Телефон: {data[2]}\n Комментарий: {data[3]}')

