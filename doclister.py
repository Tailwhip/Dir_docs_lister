import os
from openpyxl.styles import Font

def makelist(_path, _doclist, _level = 1):
    for item in os.listdir(_path):
        if os.path.isdir(_path + '/' + item):
            #print("{} jest folderem".format(item))
            _doclist.append([_path + '/', item, _level])
            new_path = _path + '/' + item
            makelist(new_path, _doclist, _level=_level+1)
        else:
            _doclist.append([_path + '/', item, _level])
    return _doclist

def exportlist(_doclist, _sheet,_kznum, _start = 1):
    style = Font(bold=True)
    for doc in _doclist:
        _sheet['A' + str(_start)] = doc[1]
        if os.path.isdir(doc[0]+doc[1]):
            print("{}-{} --> FOLDER".format(doc[1], doc[2]))
            _sheet.row_dimensions.group(_start, _start, hidden=True, outline_level=doc[2])
            _sheet['A' + str(_start)].font = style
        else:
            print("{}-{} --> plik".format(doc[1], doc[2]))
            _sheet.row_dimensions.group(_start, _start, hidden=True, outline_level=doc[2])
            if str(_sheet['B' + str(_start)].internal_value) == 'None':
                _sheet['B' + str(_start)] = _kznum
            else: _sheet['B' + str(_start)] = str(_sheet['B' + str(_start)].internal_value) + ', ' + _kznum
        _start += 1
