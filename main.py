from openpyxl import load_workbook
import kznumber as kzn
import doclister

# getting KZ number from user
kz_number = kzn.kzNumber()

# setting a path for listing documents
path = 'C:/Repozytorium/Approved/031-Pxx0/W031-Pxx0'
#'E:/Zajecia/Projekty/14-Inteligentny_pojazd/01-Mechanika'
# 'E:/Zajecia/Projekty/17-Dir_docs_lister/Dir_docs_lister'

# destination filename
dest_filename = 'W' + kz_number.kz_I + '-00-Spis_dokumentacji_wyrobu.xlsx'

wb = load_workbook(filename = 'XXX-Szablon_listy.xlsx')

sheet = wb['Lista_dokumentów']

# getting list of documents
doclister.exportlist(doclister.makelist(path, _doclist = []), sheet, kz_number.kz, _start = 2)

wb.save(dest_filename)
