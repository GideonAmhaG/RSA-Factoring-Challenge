#!/usr/bin/python3
""" RSA factorization: two prime factors """
import sys
from math import isqrt


with open(sys.argv[1], "r", encoding="utf-8") as f:
    for line in f:
        tmp = int(line)
        n = int(line)
        prime_factors = []
        sieve = [-1] * (n + 1) 
        for i in range(2, (isqrt(n) + 1)):
            if sieve[i] == -1:
                for j in range(i * i, n + 1, i):
                    if sieve[j] == -1:
                        sieve[j] = i;
        while sieve[n] != -1:
            prime_factors.append(sieve[n])
            n = n // sieve[n]
        prime_factors.append(n)
        print(prime_factors)
