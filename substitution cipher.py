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

    c = filein.read(1)
    while c != '':
        if c == ' ':  # если пробельный символ - пропускаем
            c = filein.read(1)
            continue
        fileout.write(chr(ord(c) + key))  # записываем в файл сдвинутый на key символ
        c = filein.read(1)

    filein.close()
    fileout.close()



