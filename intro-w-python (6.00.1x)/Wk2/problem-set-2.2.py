#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 10:06:59 2018

@author: evan

def calc(num):
    return round(num * (1 + annualInterestRate), 2)
print(calc(balance))
    
    if calc(updatedBal) <= payment * 12:
        print('Lowest payment: ', payment)
    else:       
        payment += 10
        return lowestPossiblePayment(payment, monthlyRate, unpaidBal, months)
"""
balance = 3298
annualInterestRate = 0.2


monthlyPayment = 0
monthlyInterestRate = annualInterestRate /12
newbalance = balance
month = 0

while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance

    for month in range(1,13):
        newbalance -= monthlyPayment
        newbalance += monthlyInterestRate * newbalance
        month += 1
print(" Lowest Payment:", monthlyPayment)