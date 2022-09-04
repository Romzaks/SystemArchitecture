import os

key = 3  # сдвиг символа на key позиций вправо, если key < 0 -> влево.


def abonent_a():
    try:
        encoder()
    except Exception as err:
        print('Exception in abonentA:' + err)


def encoder():  # зашифровывает сообщение из файла inputfile.txt, записывает в файл outputfile.txt
    filein = open('inputfile.txt', 'r')
    fileout = open('outputfile.txt', 'w')

    first_ord, last_ord = ord('a'), ord('z')
    c = filein.read(1)
    while c != '':
        if c == ' ':  # если пробельный символ - пропускаем
            c = filein.read(1)
            continue
        this_ord = ord(c) + key
        if this_ord > last_ord:
            this_ord -= (last_ord - first_ord) + 1
        fileout.write(chr(this_ord))  # записываем в файл сдвинутый на key символ
        c = filein.read(1)  # считываем новый символ

    filein.close()
    fileout.close()


def abonent_b():
    pass


abonent_a()
