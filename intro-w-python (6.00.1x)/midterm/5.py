# Write a Python function that returns a list of keys in aDict that map to
# integer values that are unique (i.e. values appear exactly once in aDict).
# The list of keys you return should be sorted in increasing order.
# (If aDict does not contain any unique values, you should return an empty list.)

# This function takes in a dictionary and returns a list.

import operator
def uniqueValues(aDict):
    '''
     aDict: a dictionary
     '''
    uniqList = []
    final = []

    for item in aDict.items():
        uniqList.append(item[1])

    copy = uniqList[:]

    for item in uniqList:
        if uniqList.count(item) > 1:
            copy.remove(item)

    for key, val in aDict.items():
        if val in copy:
            final.append(key)

    final.sort()
    return final

dict = {8: 1, 2: 4, 3: 5}

print(uniqueValues(dict))