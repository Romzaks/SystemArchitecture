# реализация алгоритма RSA

import math
import os
import random


def eiler_function(p: int, q: int):
    return (p - 1) * (q - 1)


def prime_numbers():
    flag = 1
    primes = []
    for num in range(100, 100000):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                flag = 0
                break
        if flag:
            primes.append(num)
        flag = 1
    return primes


def nod(a: int, b: int):
    if a < b:
        a, b = b, a
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


def extended_euclidean(a: int, b: int):
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
        e = random.randint(2, f - 1)
    nod1, h, d = extended_euclidean(f, e)
    print(f'{nod1} =  {f} * {h} + {e} * {d}')
    print(nod(f, e))
    #TODO 

abonent_a()




