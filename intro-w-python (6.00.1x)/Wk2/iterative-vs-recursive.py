#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Iterative vs recursive

think base + base(n-1) + base(n-2)
"""

def iterPower(base, exp):
    result = 1.0
    while exp > 0:
        result *= base
        exp -= 1
    print(result)
        

iterPower(-7.07, 6)

def recurPower(base, exp):

    if exp == 1:
        return base
    else:
        return base * recurPower(base, exp - 1)

print(recurPower(5, 3))