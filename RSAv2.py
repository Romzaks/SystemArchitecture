# реализация алгоритма RSA

import random
import os

def eiler_function(p: int, q: int):
    return (p - 1) * (q - 1)


def nod(a: int, b: int):
    """получение НОД чисел a и b"""
    if a < b:
        a, b = b, a
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


def extended_euclidean(a: int, b: int):
    """Улучшенный алгоритм Евклида для получения множителей Безу"""
    if a < b:
        a, b = b, a
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    r = r0 % r1
    while r != 0:
        r = r0 % r1
        q = (r0 - r) // r1
        r0 = r1
        r1 = r
        s = s0 - q * s1
        t = t0 - q * t1
        s0, s1 = s1, s
        t0, t1 = t1, t
    return r0, s0, t0


def abonent_a():
    """Выбираем простые числа p, q, находим n, d, выбираем e"""
    p, q = 3557, 2579

    n = p * q
    f = eiler_function(p, q)
    e = 3

    # nod1, h, d = extended_euclidean(f, e)
    d = (2 * f + 1) // e
    print(f'p = {p}, q = {q}, n = {n}, f = {f}, e = {e}, d = {d}')
    return e, n, d


def decoder(d, n, c):
    """Преобразует зашифрованное сообщение c в исходное m"""
    m = int((c ** d) % n)
    fileout = open('outputfile.txt', 'a')
    m = encoder_symbols(str(m))
    fileout.write(str(m))
    fileout.close()


def e_function(m: int, e: int, n: int):
    c = (m ** e) % n
    return c


def get_num_from_string(s: str, a: int):
    """Получение числа, меньшего чем a из строки s"""
    sum = 0
    i = 0
    for i in range(len(s)):
        if sum >= a:
            sum //= 10
            break
        num_m = int(s[i])
        sum += num_m
        if sum >= a:
            sum -= num_m
            sum //= 10
            break
        sum *= 10
        i += 1
        if i == len(s):
            sum //= 10
            break
    new_str = s[i:]
    return new_str, sum


def coder_symbols(s: str):
    """Кодировка символов числами, начиная с 11"""
    # a - 11, b - 12, ..
    s = s.lower()
    diff = ord('a') - 11
    s_ord = ''
    for i in range(len(s)):
        if s[i] == ' ':
            continue
        m_ord = ord(s[i]) - diff
        s_ord += str(m_ord)
    return s_ord


def encoder_symbols(s: str):
    """Преобразования чисел в буквы, по заданному правилу"""
    # 11 - a, 12 - b, ..
    diff = ord('a') - 11
    s_chr = ''
    for i in range(0, len(s), 2):
        m_chr = int(s[i] + s[i + 1]) + diff
        s_chr += chr(m_chr)
    return s_chr


def clear_file(filename):
    """Очистка файла filename"""
    tmp = open(filename, 'w')
    tmp.close()


def encode_symbol_in_file(filename):
    """кодирование символов в файле цифрами"""
    fileinput = open(filename, 'r')
    s = fileinput.read()
    s = coder_symbols(s)
    file = open('tmp.txt', 'w')
    file.write(s)
    file.close()
    fileinput.close()


def decode_manager(e, n, d):
    """раскодирование чисел в цифр в файле"""
    # logn = int(math.log2(n))  #взять 99
    logn = 99
    fileinput = open('tmp.txt', 'r')
    s = fileinput.read()
    s = s.strip('\n')
    while s != '':
        # print(s)
        s, c = get_num_from_string(s, logn)
        # print(c)
        c = e_function(c, e, n)
        decoder(d, n, c)
    fileinput.close()


def main():
    clear_file('outputfile.txt')
    e, n, d = abonent_a()
    encode_symbol_in_file('inputfile.txt')
    decode_manager(e, n, d)
    os.remove('tmp.txt')


main()
