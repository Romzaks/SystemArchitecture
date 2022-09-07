import os
# Шифр перестановки

key = 5  # ключ перестановки, key столбцов, передаем слева сверху по столбцам

def abonentA(): 
    try:
        matrix_of_chars, num_of_rows = init_matrix(key)  # заполнение матрицы символами
        filloutputfile(matrix_of_chars, num_of_rows, key)  # заполнение выходного файла
    except IOError:
        print('Bad files')
    except Exception as err:
        print(err)


def init_matrix(key: int):  # заполнение матрицы символами
    matrix_of_chars = [[]]

    filein = open('inputfile.txt', 'r')  # в файле находится исходное сообщение
    fileout = open('outputfile.txt', 'w')  # файл для зашифрованного сообщения

    c = filein.read(1)
    i = 0
    while c != '':  # читаем до конца файла
        if c == ' ':  # пропускаем пробелы
            c = filein.read(1)
            continue
        matrix_of_chars[i].append(c)

        if len(matrix_of_chars[i]) == key:  # заполнили строку
            c = filein.read(1)
            if c != '':
                i += 1
                matrix_of_chars.append([])
            continue

        c = filein.read(1)
            
    last_row_len = len(matrix_of_chars[i])  # если последняя строка заполнена не до конца - заполняем символом ;
    if last_row_len < 5:
        while last_row_len != 5:
            matrix_of_chars[i].append(';')
            last_row_len += 1

    filein.close()
    fileout.close()
    return matrix_of_chars, i + 1  # количество строк равно номер последней строки + 1


def filloutputfile(matrix_of_chars, num_of_rows: int, key: int):  # заполнение выходного файла
    fileout = open('outputfile.txt', 'w')

    for i in range(key):
        for j in range(num_of_rows):
            fileout.write(matrix_of_chars[j][i])


def abonentB():
    try:
        decoder(key)
    except Exception as err:
        print(err)


def count_of_chars_in_file(filename):  # считает количество символов в файле
    filein = open(filename, 'r')
    num_of_chars = 0
    c = filein.read(1)
    while c != '':
        num_of_chars += 1
        c = filein.read(1)
    filein.close()
    return num_of_chars


def decoder(key: int):  # расшифрует сообщение
    num_of_chars = count_of_chars_in_file('outputfile.txt')
    if num_of_chars % key != 0:  # округляем число символов до потолка mod key
        num_of_chars += (key - num_of_chars % key)
    num_of_rows = num_of_chars // key
    matrix_of_chars = []
    for _ in range(num_of_rows):
        matrix_of_chars.append([])

    filein = open('outputfile.txt', 'r')
    for i in range(key):
        for j in range(num_of_rows):
            matrix_of_chars[j].append(filein.read(1))  # заполнение матрицы символов

    out = open('out.txt', 'w')
    for i in range(num_of_rows):
        for j in range(key):
            if matrix_of_chars[i][j] == ';':  # записываем расшифрованный текст в файл, пропуская символ ';'
                continue
            out.write(matrix_of_chars[i][j])
    out.close()
    filein.close()

    flag = True  # что делаем с файлами дальше
    if flag:
        os.remove('outputfile.txt')
        os.rename('out.txt', 'outputfile.txt')  # переименовываем файл, удаляем зашифрованное сообщение
    else: 
        os.rename('out.txt', 'outfile.txt')  # если необходимо проверить зашифрованное сообщение


abonentA()
abonentB()
