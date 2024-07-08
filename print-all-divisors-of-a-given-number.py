# NUMBER OF APPROACHES: TWO

from math import sqrt

# O(n)
############################################################################
'''
Algorithm explanation

We start from 1 and go till n, checking for each number if it divides n.
'''
def brute_force():
    num = int(input())
    factors = []
    for i in range(1, num + 1):
        if (num % i == 0): # if divisor
            factors.append(i) # add it in asnwer array
    print(factors)
############################################################################
'''
Complexity explanation

The loop runs from 1 to n hence TC is O(n)
'''


# O(sqrt(n))
############################################################################
'''
Algorithm explanation

We start from 1 and go till sqrt(n), checking for each number if it divides n.
Why? explained in TC analysis.
'''
def optimal():
    num = int(input())
    factors = []
    for i in range(1, int(sqrt(num)) + 1):
        if (num % i == 0): # if divisor
            factors.append(i) # add it
            # add the counterpart (eg 4 . 9 = 36, so 9 is counterpart of 4)
            if (i != num // i): # avoiding double entry for perfect squares (eg 6 . 6 = 36)
                factors.append(num // i)
    print(factors)
############################################################################
'''
Complexity explanation

For any positive number n, the factors of n are symmetrical around sqrt(n). For eg
1 . 36 = 36
2 . 18 = 36
3 . 12 = 36
4 . 9 = 36
6 . 6 = 36 (sqrt 36 = 6)
----------repetition starts---------
9 . 4 = 36
12 . 3 = 36
18 . 2 = 36
36 . 1 = 36

So, we stop at sqrt(n).
'''