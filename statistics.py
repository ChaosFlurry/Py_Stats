from math import *
from probability import *

#https://www.wolframalpha.com/examples/math/statistics/


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


def invnormal(x, mu, sigma):
    #https://mymerchinfo.com/ibi_help/index.jsp?topic=%2Fcom.ibi.help.functions%2Fsource%2Fnumeric13.htm
    #https://support.microsoft.com/en-us/help/827358/excel-statistical-functions-norminv

    #http://commons.apache.org/proper/commons-math/

    #l = (mu ** 3) / (sigma ** 2)
    l = 1 / sigma
    return ((l / (2 * pi * (x ** 3))) ** 0.5) * exp((-1) * l * ((x - mu) ** 2) / (2 * (mu ** 2) * x))


    #return ((mu ** 1.5) / ((2 * pi * (sigma ** 2) * (area ** 3)) ** 0.5)) * exp((-1) * (mu ** 3) * ((area - mu) ** 2) / (2 * (sigma ** 2) * (mu ** 2) * area))
    #return (((mu ** 3) / (2 * pi * (sigma ** 2) * (area ** 3))) ** 0.5) * exp(((-1) * (mu ** 3) * ((area - mu) ** 2)) / (2 * (sigma ** 2) * area))
    #1 / sqrt(sigma ^ 2 * 2pi) * e ^
    #lambda = u3 / sigma2


def poissonpdf(mu, x):
    return (mu ** x) * exp((-1) * mu) / factorial(x)


def poissoncdf(mu, l, u):
    result = 0
    for i in range(l, u + 1):
        result += poissonpdf(mu, i)
    return result


