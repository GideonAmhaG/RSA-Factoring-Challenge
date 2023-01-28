#!/usr/bin/python3
""" RSA factorization: two prime factors """
import sys


def isPrime(n, k=5):
    """ miller-rabin """
    from random import randint
    if n < 2: return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0: return n == p
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s + 1, d // 2
    for i in range(k):
        x = pow(randint(2, n - 1), d, n)
        if x == 1 or x == n - 1: continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1: return False
            if x == n - 1: break
        else: return False
    return True


def factors(n, b2=-1, b1=10000):
    """ 2,3,5-wheel, then rho """
    def gcd(a, b):
        """ euclid's algorithm """
        if b == 0: return a
        return gcd(b, a % b)

    def insertSorted(x, xs):
        """ linear search """
        i, ln = 0, len(xs)
        while i < ln and xs[i] < x: i += 1
        xs.insert(i, x)
        return xs
    if -1 <= n <= 1: return [n]
    if n < -1: return [-1] + factors(-n)
    wheel = [1, 2, 2, 4, 2, 4, 2, 4, 6, 2, 6]
    w, f, fs = 0, 2, []
    while f * f <= n and f < b1:
        while n % f == 0:
            fs.append(f)
            n //= f
        f, w = f + wheel[w], w + 1
        if w == 11: w = 3
    if n == 1: return fs
    h, t, g, c = 1, 1, 1, 1
    while not isPrime(n):
        while b2 != 0 and g == 1:
            h = (h * h + c) % n
            h = (h * h + c) % n
            t = (t * t + c) % n
            g = gcd(t - h, n); b2 -= 1
        if b2 == 0: return fs
        if isPrime(g):
            while n % g == 0:
                fs = insertSorted(g, fs)
                n //= g
        h, t, g, c = 1, 1, 1, c+1
    return insertSorted(n, fs)


with open(sys.argv[1], "r", encoding="utf-8") as f:
    for line in f:
        n = int(line)
        pfs = factors(n)
        if len(pfs) == 2:
            print("{}={}*{}".format(n, pfs[1], pfs[0]))
