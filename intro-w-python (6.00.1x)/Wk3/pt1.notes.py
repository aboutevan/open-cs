
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

