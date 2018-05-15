#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
balance
annualInterestRate
monthlyPaymentRate

	      # Test Case 1:
	      balance = 42
	      annualInterestRate = 0.2
	      monthlyPaymentRate = 0.04
	      
"""
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

rt = annualInterestRate / 12

counter = 0  
def printBal(bal, interest, rate, counter):
    payment = bal * rate
    unpaidBal = bal - payment
    updatedBal = round(unpaidBal + rt * unpaidBal, 2)
    counter += 1
    
    if counter < 12:   
        return printBal(updatedBal, interest, rate, counter)
        
    print('Remaining balance: ', updatedBal)
        


printBal(balance, annualInterestRate, monthlyPaymentRate, counter)
