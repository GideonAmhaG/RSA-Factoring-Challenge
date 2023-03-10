#!/usr/bin/python3
""" RSA factorization: simply factorize """
import sys


with open(sys.argv[1], "r", encoding="utf-8") as f:
    for line in f:
        n = int(line)
        p = 2
        q = 0
        while p**2 <= n:
            if n % p == 0:
                q = n // p
                print("{:d}={:d}*{:d}".format(n, q, p))
                break
            else:
                p += 1
