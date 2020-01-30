from math import sqrt

def primes(start, end):
    primes = [x for x in range(start, end + 1)]
    N = int(sqrt(end))
    for i in range(2, N+1):
        for num in primes:
            if num == 1 or num % i == 0 and num is not i:
                primes.remove(num)
    return primes
