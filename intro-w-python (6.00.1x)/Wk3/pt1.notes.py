
"""
TUPLES 
    - an ordered sequence of elements, can mix element types
    - IMMUTABLE
    - represented with parentheses
    - i.e
        - te = ()
        - t = (2, "one", 3)
        - t[0] is 2
        - ('one',) - need comma to indicate a tuple of one
        
    - conviently used to swap variables
        (x, y) = (y, x)

    - used to return more than one value from a function
    
def get_data(aTuple):
    nums = ()
    words = ()

    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
            
    min_nums = min(mums)
    max_nums = max(nums)
    unique_words = len(words)
    
    return (min_nums, max_nums, unique_words)
    
(small, large, words = get_data(((1, 'mine'),
                                 (3, 'yours'),
                                 (5, 'ours')))
"""


def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    myTup = ()
    for idx, el in enumerate(aTup):
        if idx % 2 is 0:
            myTup = myTup + (el,)
    return myTup

print(oddTuples(('I', 'am', 'a', 'test', 'tuple')))

"""
LISTS

    - ordered sequence, accesible by index
    - denoted by square brackets []
    - usually homogenous elements, but can be mixed (not common)
    - MUTABLE
    
    a_list = []
    b_list = [2, 'a', 5, True]
    
    L = [2,1,3]
    
    L[1] = 5 --- mutable
    
    Operations on LISTS:
        
        - L.append(4)
            - MUTATES THE STATE
        
        - L3 = L1 + L2
            - concatenate - doesn't mutate
        
        - L1.extend(L2)
            - this does mutate
            
        - del(L[index])
        
        - pop() - returns removed elemet
        
        - L.remove(element)
            - removes first occurence of element in list
            
        - list(s)
            - convert string to list with each char as separate el
            
        - s.split(divider)
            - convert string to list, split at divider
            
        - ''.join(L)
            - returns "abc"
        
        - '_'.join(L)
            - returns "a_b_c"
            
        - L.sort()
            - mutates and sorts
            
        - sorted(L)
            returns a sorted list (not mutated)
            
        - L.reverse()
            - reverse and mutate
            
        - range()
            - returns something that behaves like a tuple!
            
            range(5) => equal to tuple [0,1,2,3,4]
            range(2,6) => equal to tuple [2,3,4,5]
            range(5,2,-1) => equal to tuple [5,4,3]
            
            - when using range in for loop, loop variable iterates over something
              similar to a list
        
"""

"""
Mutation, Aliasing, Cloning

pythontutor.com

- copying a list

    cool = ['blue', 'green']
    
    // make a copy
    chill = cool[:]
    
    // if you do
    chill = cool
    // then that doesn't make a copy, it points to same reference, so any changes to either will be applied to other
    
- AVOID mutating a list as you iterate over it 
    - mutating list can change the list length
    - python doesn't update the index counter if the list changes
    - therefore some elements could be skipped over
    
def remove_dups(L1, L2):
    L1_copy = L1[:] // make a copy of it instead of changing directly, to avoid above issue
    for e in L1_copy:
        if e in L2:
            L1.remove(e)

"""

"""
Functions as objects, dictonaries

functions are first class objects
 - has types
 - can be elements of data structures like list
 - can appear in expressions
    - as part of an assignment statement
    - as an argument to a function!!
    
- particularly useful to use functions as arguments when coupled with lists
    - aka higer order programming
    
GENERALIZATION OF HOPS

- map

- map(abs, [x,y,z])
    - or map(min, [1,39,44], [4,18,99]) // will compare each element in list and return min

- map returns something similar to a list - have to walk down


"""

"""
STRINGS, LISTS, TUPLES, RANGES

    - common ops
    
        - seq[i]
        - len(seq)
        - seq1 + seq2 - concatenation of sequences (not range)
        - n*seq - sequence that repeats seq n times (not range)
        - seq[start:end] - slice of sequence
        - e in seq - true if e contained in seq
        - e not in seq true if not seq
        - for e in seq - iterates over elements in sequence

DICTIONARIES - similar to obj in JS?

    - index item of interest directly
    - use one data structure, not separate lists
    
    - my_dict = {}
    
        grades = {'Ana': 'B', 'John': 'A+'}
        
        grades['John'] returns 'A+'
        
        so el, grades[el]

    - operations
    
        add -- grades['Sylvan'] = 'A'
        test -- 'John' in grades
        delete -- del(grades['Ana'])
        keys -- grades.keys() -- returns ['Ana', 'John']
        values -- grades.values() -- ['B', 'A+']
        

"""
# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
#
# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')

# def how_many(aDict):
#     '''
#     aDict: A dictionary, where all the values are lists.
#
#     returns: int, how many values are in the dictionary.
#     '''
#     values = aDict.values()
#     total = []
#     for val in values:
#         total = total + val
#     return len(total)
#
#
# print(how_many(animals))


# We want to write some simple procedures that work on dictionaries to return information.
#
# This time, write a procedure, called biggest, which returns the key corresponding to the entry with
#  the largest number of values associated with it. If there is more than one such entry,
# return any one of the matching keys.

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggest = 0
    key = ''
    for a in aDict:
        if len(aDict[a]) >= biggest:
            key = a
            biggest = len(aDict[a])
    return key


biggest(animals);

"""
FIBONACCI WITH DICTIONARY

def fib_efficient(n, d):
    
    if n in d:
        return d[n]
        
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[ans] = ans
        return ans
        
d = {1:1, 2:2}
print(fib_efficient(6, d))

- do a lookup first in case already calculated the value
- modify dictionary as progress through function calls

"""
