import os
import openpyxl
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl import load_workbook
import kznumber as kzn
import os


dir_end = False
path = 'E:/Zajecia/Projekty/14-Inteligentny_pojazd/01-Mechanika'
# 'E:/Zajecia/Projekty/17-Dir_docs_lister/Dir_docs_lister'
# 'E:/Zajecia/Projekty/14-Inteligentny_pojazd/01-Mechanika'

kz_number = kzn.kzNumber()

def list(_path):
    for item in os.listdir(_path):
        if os.path.isdir(_path + '/' + item):
            print("{} jest folderem".format(item))
            new_path = _path + '/' + item
            list(new_path)
        else: print("{} jest plikiem".format(item))

list(path)

'''
for item in os.listdir(path):

'''
# destination filename
dest_filename = kz_number.kz_I + '-Lista_dokumentów.xlsx'

wb = load_workbook(filename = 'XXX-Lista_dokumentów.xlsx')

sheet = wb['Lista_dokumentów']

sheet.row_dimensions.group(4, 15, hidden = True)

sheet['A11'] = "Twoja stara"

sheet.row_dimensions.group(11, 14, hidden = True, outline_level=2)

wb.save(dest_filename)