"""
TESTING and DEBUGGING

- make programs modular
- document constraints on modules
    - what do you expect input to be? the output?

- document assumptions
    - what assumptions are behind the code design?

Ready to test?

- create a set of different types of inputs

CLASSES OF TESTS

- UNIT TESTING
    - validate each piece of program
    - testing each function separately

- REGRESSION TESTING
    - add test for bugs as you find them in a function
    - catch reintroduced errors that were previously fixed

- INTEGRATION TESTING
    - does overall program work?
    - many tend to rush to do this which is obvs bad

APPROACHES TO TESTING
 - intuition
 - random testing

 - black box testing
    - explore paths through specification
    - designed without looking at the code

 - glass box testing
    - explore paths through code
    - use code directly to guide the design of test cases
    - called path-complete if every potential path through code is tested at least once
    - drawbacks:
        - go through loops arbitrarily
        - missing paths
    - guidelines:
        -branches
        - for loops
        - while loops

==========================
BUGS

- Overt
    - obvious indication something is wrong

- Covert
    - has no obvious manifestation - code returns value, but it's wrong

- Persistent
    - occurs every time code is run

- Intermittent
    - occurs only some times

ERROR MESSAGES

- IndexError
    - beyond limits of test

-TypeError
    - trying to convert inappropriate type

-NameError
    - referencing a non-existent variable

-TypeError
    - mixing data types w/o appropriate coercion

-SyntaxError
    - forgetting to close a parenthesis, quotation, etc.

"""

"""
EXCEPTIONS, ASSERTIONS

try:
 // nani nai

except ValueError:
    print("Value error handle")
    
except ZeroDivisionError:
    // etc.
 
except:
    print("Error")

else:
    - executed when associated try body completes with no exceptions

finally:
    - always executed after try, else and except clauses,
    even id they raised another error or executed a break, continue or return
    - useful for clean upcode that should be run no matter what


EXCEPTION AS CONTROL FLOW

- don't return a special error value and then check for that value
- instead, raise an exception when unable to produce a consistent result

"""

"""
ASSERTIONS
    
    - want to be sure that assumptions on state of computation are expected 
    - use an assert statement to raise an AssertionError exception if assumptions are not met
    - good ex of defensive programming
    
def avg(grades):
    assert not len(grades) == 0,
    return sum(grades)/len(grades)
    
    - dont' allow programmer to control response to unexpected condtions
    - ensure that execution halts whenever an expected condition is not met
    - typically used to check in puts to functions procedures, but can be used anywhere
    - can be used to check the outputs of a function to avoid propagating bad values
    - can make it easier to locate the source of a bug
    
    - use assertions to:
        - check types
        - check that invariants on data structures are met
        - check constraints on return values
        - check for violations of constraints on procedure

"""