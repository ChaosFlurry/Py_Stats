from math import *
from probability import *


def binompdf(n, p, x):
    return ncr(n, x) * (p ** x) * ((1 - p) ** (n - x))


def binomcdf(n, p, l, u):
    result = 0
    for i in range(l, u + 1):
        result += binompdf(n, p, i)
    return result


def normalpdf(mu, sigma, x):
    return (1 / ((2 * pi * (sigma ** 2)) ** 0.5)) * exp((-1) * ((x - mu) ** 2) / (2 * (sigma ** 2)))


def normalcdf(mu, sigma, l, u):
    return 0.5 * (erf((u - mu) / ((2 ** 0.5) * sigma)) - erf((l - mu) / ((2 ** 0.5) * sigma)))


def poissonpdf(mu, x):
    return (mu ** x) * exp((-1) * mu) / factorial(x)


def poissoncdf(mu, l, u):
    result = 0
    for i in range(l, u + 1):
        result += poissonpdf(mu, i)
    return result


