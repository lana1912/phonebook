import controller 

select = input('нажмите "1"/"2"):')

if select == '1': 
    controller.phone_book_line()
    controller.pri()

if select == '2': 
    controller.phone_book_column()
    controller.pri2()


