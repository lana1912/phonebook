from write_phone import data

def read_csv_line(a):
    data = open('Fhonebook.csv', 'r')
    a = [line.strip() for line in data.readlines()]
    print(f'Имя: {a[1]} Фамилия: {a[2]} Телефон: {a[3]} Комментарий: {a[4]}')

def read_csv_column(a):
    data = open('Fhonebook.csv', 'r')
    a = [line.strip() for line in data.readlines()]
    print(f'Имя: {a[1]}\nФамилия: {a[2]}\nТелефон: {a[3]}\nКомментарий: {a[4]}')

