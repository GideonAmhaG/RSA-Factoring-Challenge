#!/usr/bin/python3
""" RSA factorization: two prime factors """
import sys
import math as mt


with open(sys.argv[1], "r", encoding="utf-8") as f:
    for line in f:
        n = int(line)
        MAXN = int(line) + 1
        spf = [0 for i in range(MAXN)]
        prime_factors = []
        for i in range(2, MAXN):
            spf[i] = i
        for i in range(4, MAXN, 2):
            spf[i] = 2
        for i in range(3, mt.ceil(mt.sqrt(MAXN))):
            if (spf[i] == i):
                for j in range(i * i, MAXN, i):
                    if (spf[j] == j):
                        spf[j] = i
        while n != 1:
            prime_factors.append(spf[n])
            n = n // spf[n]
        print(prime_factors)
