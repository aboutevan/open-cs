"""


"""
def genPrimes():
    x = 2
    primes = [2]

    yield x
    while True:
        x += 1
        if all((x % p) != 0 for p in primes):
            primes.append(x)
            yield x

x = genPrimes()

x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()
x.__next__()