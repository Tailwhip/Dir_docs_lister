from openpyxl import load_workbook
import kznumber as kzn
import doclister

# getting KZ number from user
kz_number = kzn.kzNumber()

# setting a path for listing documents
path = 'E:/Zajecia/Projekty/14-Inteligentny_pojazd/01-Mechanika'
# 'E:/Zajecia/Projekty/17-Dir_docs_lister/Dir_docs_lister'

# destination filename
dest_filename = kz_number.kz_I + '-Lista_dokumentów.xlsx'

wb = load_workbook(filename = 'XXX-Lista_dokumentów.xlsx')

sheet = wb['Lista_dokumentów']

# getting list of documents
doclister.exportlist(doclister.makelist(path, _doclist = []), sheet, _start = 2)

wb.save(dest_filename)
