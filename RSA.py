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


def abonent_a():
    primes = prime_numbers()
    p, q = primes[random.randint(0, len(primes) - 1)], primes[random.randint(0, len(primes) - 1)]
    while p == q:
        q = primes[random.randint(0, len(primes) - 1)]

    n = p * q
    f = eiler_function(p, q)
    e = random.randint(1, f - 1)
    while (f % e) == 0:
        e = random.randint(1, f - 1)
    print(p, q)
    print(e, f)




