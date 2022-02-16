from write_phone import data

from user_interface import console_line
from user_interface import console_colunm
data = 'Fhonebook.csv'

def read_csv():
    with open(data, 'r') as rd:
        #rd.readlines()
        for i in rd:
            console_line(i.split(';'))
            

def read_csv_colunm():
    with open(data, 'r') as rd:
        #rd.readlines()
        for i in rd:
            console_colunm(i.split(';'))
            

           