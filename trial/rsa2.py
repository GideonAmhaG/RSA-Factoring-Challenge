#!/usr/bin/python3
""" RSA factorization: two prime factors """
import sys


with open(sys.argv[1], "r", encoding="utf-8") as f:
    for line in f:
        tmp = int(line)
        n = int(line)
        div = 2
        prime_factors = []
        while div**2 <= n:
            if n % div == 0:
                prime_factors.append(div)
                n //= div
            else:
                div += 1
        prime_factors.append(n)
        if len(prime_factors) == 2:
            print("{}={}*{}".format(tmp, prime_factors[1], prime_factors[0]))
