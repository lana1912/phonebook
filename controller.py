import write_phone
import read_book
import user_interface as ui

def phone_book_line():
    name = ui.name()
    surname = ui.surname()
    phone = ui.phone()
    comment = ui.comment()
    result = write_phone.write_line(name, surname, phone, comment)
    read_book.read_csv_line(result)
    

def phone_book_column():
    name = ui.name()
    surname = ui.surname()
    phone = ui.phone()
    comment = ui.comment()
    write_phone.write_column(name, surname, phone, comment)
    read_book.read_csv_column()
    