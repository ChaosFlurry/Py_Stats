from math import factorial


def npr(n, r):
    return factorial(n) / factorial(n - r)


def ncr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))
