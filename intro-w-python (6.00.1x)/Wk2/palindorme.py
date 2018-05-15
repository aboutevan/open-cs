#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Palindromes

convert string to characters, by stripping out punc and converting
upper case to to lower case

Base case: string of length 0 or 1

then check if first and last are the same
"""

def isPalindrome(s):
    
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
        
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))
