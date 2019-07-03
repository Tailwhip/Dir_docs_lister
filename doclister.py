import os
from openpyxl.styles import Font

# making a list of documents where: _doclist[0] is a doc path, [1] is a doc name, [2] is a group level
def makedoclist(_path, _doclist, _level = 1):
    for name in os.listdir(_path):
        if os.path.isdir(_path + '/' + name):
            _doclist.append([_path + '/', name, _level])
            new_path = _path + '/' + name
            makedoclist(new_path, _doclist, _level=_level+1)
        elif os.path.isfile(_path + '/' + name):
            _doclist.append([_path + '/', name, _level])
    return _doclist

def exportlist(_doclist, _sheet,_kznum, _start = 1):
    style = Font(bold=True)
    for doc in _doclist:
        _sheet['A' + str(_start)] = doc[1]
        if os.path.isdir(doc[0]+doc[1]):
            #print("{}-{} --> FOLDER".format(doc[1], doc[2]))
            _sheet.row_dimensions.group(_start, _start, hidden=True, outline_level=doc[2])
            _sheet['A' + str(_start)].font = style
        else:
            #print("{}-{} --> plik".format(doc[1], doc[2]))
            _sheet.row_dimensions.group(_start, _start, hidden=True, outline_level=doc[2])
            if str(_sheet['B' + str(_start)].internal_value) == 'None':
                _sheet['B' + str(_start)] = _kznum
            else: _sheet['B' + str(_start)] = str(_sheet['B' + str(_start)].internal_value) + ', ' + _kznum
        _start += 1
    print("LIST IS DONE")

def makelist(_doclist, _sheet, _start = 2):
    while str(_sheet['A' + str(_start)].internal_value) != 'None':
        _doclist.append(_sheet['A' + str(_start)].internal_value)
        _start += 1
    #for item in _doclist:
     #   print(item)
    print('OLD LIST DONE')
    return _doclist

def convtonamelist(_doclist):
    newlist = []
    for doc in _doclist:
        newlist.append(doc[1])
    #for item in newlist:
     #   print(item)
    print('NEW LIST DONE')
    return newlist

def evenlists(_oldlist, _newlist):
    # make both list length even by adding blank values at the end of shorter one
    if _oldlist.__len__() < _newlist.__len__():
        for i in range(_newlist.__len__() - _oldlist.__len__()):
            _oldlist.append('')
    elif _oldlist.__len__() > _newlist.__len__():
        for i in range(_oldlist.__len__() - _newlist.__len__()):
            _newlist.append('')

def wordtolist(word):
    list = []
    for letter in word:
        list.append(letter)
    return list

def comparelists(_oldlist=[], _newlist=[]):
    evenlists(_oldlist, _newlist)
    letters_limit = 4
    # comare document lists
    for i, doc in enumerate(_newlist):
        print(str(i) + '. OLD ' + _oldlist[i])
        print('                                                        ' + str(i) + '. NEW ' + doc)
        # if document in one list is the same as in second then do nothing
        # but if not then compare letter after letter and check how many consecutive letters match
        if doc == _oldlist[i]:
            pass
        else:
            # convert each document name to list and even the lists length
            olddoc = wordtolist(_oldlist[i])
            doc = wordtolist(doc)
            evenlists(olddoc, doc)
            '''
            for letter in olddoc:
                print(letter)

            for letter in doc:
                print('                          ' + letter)'''
            letters_counter = 0
            matching_letter = True
            # counting consecutive letters
            for j, letter in enumerate(doc):
                if letter == olddoc[j] and matching_letter == True:
                    letters_counter += 1
                else:
                    matching_letter = False

            if letters_counter > letters_limit:


            print(str(i) + '. matching letters: ' + str(letters_counter))
            break




