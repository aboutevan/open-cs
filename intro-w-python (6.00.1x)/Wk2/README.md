Converting Decimal to Binary

Binary code represents text, computer processor instructions, or any other data using a two-symbol system, typically 0 and 1's.

Coverting a number to binary is simple:

###Fuctions in Python

- can access global vars inside a func
- **cannot modify** a global var inside function

```
def is_even(i):
	"""
	Input: i, positive int
	Returns True if i is even, otherwise False
	"""
	print("hi")
	return i%2 == 0

is_even(3)	
```

###Recursion
- when a function calls itself
- break a program down into a small problem and act upon the result

```
def recurPower(base, exp):

    if exp == 1:
        return base
    else:
        return base * recurPower(base, exp - 1)

print(recurPower(5, 3))
```

##Mathematical Induction
To prove a statement indexed on integers is true for all values of n:

- prove it is true when n is smallest value (e.g. n= 0 or n=1)
- Then prove that if it is true for an arbitrary value of n, one can show that it must be true for n+1
- Check in recursion