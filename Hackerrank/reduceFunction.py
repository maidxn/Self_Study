from fractions import Fraction
from functools import reduce
from math import gcd

def product(fracs):
    numerator = reduce(lambda x, y: x * y, list(fracs[i].numerator for i in range(len(fracs))))
    denominator = reduce(lambda x, y: x * y, list(fracs[i].denominator for i in range(len(fracs))))
    div = reduce(gcd, [numerator, denominator])
    t = Fraction(numerator//div, denominator//div)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)