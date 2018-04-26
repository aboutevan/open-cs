#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BISECTION SEARCH

radically reduces computation time

should work well with "ordering" property - 
    value of function being solved varies monotonically with input value
    function g**2; grows as g grows
"""
# sq root bisection
x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))