# реализация алгоритма RSA

import math
import os
import random


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
    p, q = 3557, 2579

    n = p * q
    f = eiler_function(p, q)
    e = 3

    #nod1, h, d = extended_euclidean(f, e)
    d = (2 * f + 1) // e
    print(f'p = {p}, q = {q}, n = {n}, f = {f}, e = {e}, d = {d}')
    return e, n, d


def decoder(d, n, c):
    m = int((c ** d) % n)
    fileout = open('outputfile.txt', 'a')
    m = encoder_symbols(str(m))
    fileout.write(str(m))
    fileout.close()


def e_function(m: int, e: int, n: int):
    c = (m ** e) % n
    print('C ==', c)
    return c


def get_num_from_string(s, a):
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
    #11 - a, 12 - b, ..
    diff = ord('a') - 11
    s_chr = ''
    for i in range(0, len(s), 2):
        m_chr = int(s[i] + s[i + 1]) + diff
        s_chr += chr(m_chr)
    return s_chr


def main():
    fileout = open('outputfile.txt', 'w')
    fileout.close()
    e, n, d = abonent_a()
    #logn = int(math.log2(n))  #взять 99
    logn = 99
    fileinput = open('inputfile.txt', 'r')
    s = fileinput.read()
    s = coder_symbols(s)
    file = open('tmp.txt', 'w')
    file.write(s)
    file.close()
    fileinput.close()
    os.remove('inputfile.txt')
    os.rename('tmp.txt', 'inputfile.txt')
    fileinput = open('inputfile.txt', 'r')
    s = fileinput.read()
    s = s.strip('\n')
    print(logn)
    while s != '':
        print(s)
        s, c = get_num_from_string(s, logn)
        print(c)
        c = e_function(c, e, n)
        decoder(d, n, c)
    fileinput.close()


main()
