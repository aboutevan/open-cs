#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Iterative vs recursive
"""

def gcdIter(a, b):

    if (a <= b):
        guess = a
    else:
        guess = b

    while a % guess != 0 or b % guess !=0:
        guess = guess - 1

    return guess

print(gcdIter(17,12))
        

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
print(gcdRecur(27,12))
    
