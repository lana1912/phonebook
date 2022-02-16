data = 'Fhonebook.csv'

def write_line(name, surname, phone, comment):
    global data
    file1 = data
    with open(file1, 'a') as f:
        f.write(f'{name};{surname};{phone};{comment}')
        #f.write('')
    return file1


def write_column(name, surname, phone, comment):
    global data
    file2 = data
    with open(file2, 'a') as f:
        f.write(f'{name};\n{surname};\n{phone};\n{comment};')
        #f.write('')
    return file2
