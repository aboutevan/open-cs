#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''

bob = 'bob'
i = 0
occurs = 0
s= 'azcbobobegghakl'

for letter in s:
    if s[i:i+3] == bob:        
        occurs += 1
    i +=1
print('Number of times bob occurs is: ' + str(occurs))