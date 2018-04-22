#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 07:16:46 2018

@author: evan
"""

print("Hello World")
num = 2
while num <= 10:
    print(num)
    num += 2
print("Goodbye!")

x = 0
y = x
end = 6
while x < end:
    x += 1
    y += x
print(y)

for x in range(2,11,2):
    print(x)
print("Goodbye!")

total = 0

for current in range(1, end + 1):
    total += current
print(total)

num = 10
for num in range(5):
    print(num)
print(num)

if 16 % 16 == 0:
    print('ue')
for letter in 'hola':
    print(letter)  