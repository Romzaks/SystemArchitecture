# реализация алгоритма RSA

import math
import os
import random


def eiler_function(p: int, q: int):
    return (p - 1) * (q - 1)


def prime_numbers():
    """Возвращает список всех простых чисел от a до b"""
    a, b = 100, 9999
    flag = 1
    primes = []
    for num in range(a, b):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                flag = 0
                break
        if flag:
            primes.append(num)
        flag = 1
    return primes


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
    primes = prime_numbers()
    p, q = primes[random.randint(0, len(primes) - 1)], primes[random.randint(0, len(primes) - 1)]
    while p == q:
        q = primes[random.randint(0, len(primes) - 1)]

    n = p * q
    f = eiler_function(p, q)
    e = random.randint(1, f - 1)

    while nod(f, e) != 1:
        e = random.randint(2, 66000)
    nod1, h, d = extended_euclidean(f, e)
    d = (2 * f + 1) // e  # ???
    print(f'p = {p}, q = {q}, n = {n}, f = {f}, e = {e}, d = {d}')
    return e, n, d


def decoder(d, n, c):
    m = (c ** d) % n
    fileout = open('outputfile.txt', 'a')
    fileout.write(str(m))
    fileout.close()


def e_function(m: int, e: int, n: int):
    c = (m ** e) % n
    return c


def get_num_from_string(s, a):
    sum = 0
    i = 0
    num_m = 0
    for m in s:
        if sum >= a:
            break
        num_m = int(m)
        sum += num_m
        if sum >= a:
            break
        sum *= 10
        i += 1
    sum /= 10
    sum -= num_m
    new_str = s[i:]
    return new_str, sum


def main():
    fileout = open('outputfile.txt', 'w')
    fileout.close()
    e, n, d = abonent_a()
    logn = int(math.log2(n))
    fileinput = open('inputfile.txt', 'r')
    s = fileinput.read()
    print(logn)
    while s != '':
        s, c = get_num_from_string(s, logn)
        decoder(d, n, c)
    fileinput.close()


main()

