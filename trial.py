#!/usr/bin/python3
""" RSA factorization: two prime factors """
import sys
import math


def fact(n):
    pfs = []
     
    while n % 2 == 0:
        pfs.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            pfs.append(i)
            n = n // i
    if n > 2:
        pfs.append(n)
    return pfs

with open(sys.argv[1], "r", encoding="utf-8") as f:
    for line in f:
        n = int(line)
        pfs = fact(n)
        if len(pfs) == 2:
            print("{}={}*{}".format(n, pfs[1], pfs[0]))
	
