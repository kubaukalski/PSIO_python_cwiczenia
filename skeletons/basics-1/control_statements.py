#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# TEMAT: Instrukcje sterujące
#
# -----------------------------------------------------------------------------


def parity_str(n: int) -> str:
    return "parzysta" if n % 2 == 0 else "nieparzysta"


def plf(x: float) -> float:
    if x < 3:
        return 1
    elif x < 10:
        return 1.5
    else:
        return 4


def factorial(n: int) -> int:
    if n == 0:
        return 1
    for i in range(1, n):
        n *= i
    return n


def min_pow_2(n: int) -> int:
    i = 0
    while n // 2 > 0:
        n //= 2
        i += 1
    return 2 ** (i+1)
