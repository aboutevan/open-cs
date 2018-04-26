#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 20:10:23 2018

@author: evan
"""


low = 0
high = 100

guess = int((low + high) / 2)

print('Please think of a number between 0 and 100!')
print('Is your secret number ' + str(guess) + '?')
userAns = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

while userAns != 'c':
    
    if userAns != 'h' and userAns != 'c' and userAns != 'l':
       print('Sorry, I did not understand your input.') 
    if userAns == 'h':
        high = guess
    elif userAns == 'l':
        low = guess
    guess = int((low + high) / 2)
    
    print('Is your secret number ' + str(guess) + '?')
    userAns = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

print('Game over. Your secret number was:', guess)
