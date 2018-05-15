#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Base case: check if test character is same as middle character
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    original = aStr;

    middle = aStr[int(len(aStr) / 2)]

    if char == middle:
        print(True)
        return True
    elif char != middle and len(aStr) == 1:
        return False
 
    if char < middle:
        aStr = original[0:original.find(middle)]
    else:
        aStr = original[original.find(middle):]
    print(char, aStr)
    return isIn(char, aStr)

strs = 'cdefgh'

isIn('pf', 'fip')