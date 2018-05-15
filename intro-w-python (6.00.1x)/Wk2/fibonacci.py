#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Base cases: 0 or 1
returns fibonacci of x
"""

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
