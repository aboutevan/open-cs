"""
PROGRAM EFFICIENCY

- Order of Growth
    - evaluate program's efficiency when input is very big
    - express growth of program's run time as input size grows
    - put upper bound on growth
    - do not need to be precise
    - look at largest factors in run time

    - constant, linear, quadratic, logarithmic, n log n, exponential

"""

"""
BIG OH

- measures the upper bound on the asymptotic growth, aka order of growth
- Big Oh or O() is used to describe the worst case
    - worst case occurs often and is bottleneck when a program runs
    - express rate of growth of program relative to input size
    - evaluate algorithm not machine or implementation
    
    - drop constants and multiplicative factors
    - focus on dominant terms
    
- O(1): constant
- O(log n): logarithmic
- O(n): linear
- O(n log n): loglinear
- O(n^c): polynomial
- O(c^n): exponential (c is constant)

- combine complexity classes
     - analyze statements inside functions
     - apply some rules, focus on dominant term
 
 - Law of Addition for O():
    - used with sequential statements
    - O(f(n)) + O(g(n)) is O(f(n) + g(n))
    
    for example:
        for i in range(n):
            print('a')
        for j in range(n*n):
            print('b')
    
    is O(n) + O(n*n) = O(n + n^2) = O(n^2) because of dominant term
    
- Law of Multiplication for O():
    - used with nested statements/loops
    - O(f(n)) * O(g(n)) is O(f(n) * g(n))
    
    for example:
        for i in range(n):
            for j in range(n):
                print('a')
    is O(n)*O(n) = O(n*n) = O(n^2) because the outer loop goes n times and the 
    inner loop goes n times for every outer loop
"""