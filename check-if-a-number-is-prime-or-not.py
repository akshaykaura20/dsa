# NUMBER OF APPROACHES: ONE 

# (brute force is too easy)

from math import sqrt

# O(sqrt(n))
############################################################################
'''
Algorithm explanation

We start from 2 and go till sqrt(n), checking for each number if it divides n. 
If 0 divisors, then its prime!
Why till sqrt(n)? explained in TC analysis.
'''
def optimal():
    num = int(input())
    for i in range(2, int(sqrt(num)) + 1):
        if (num % i == 0): # if divisor
            print("NOT prime!")
            exit(1)
    print("Prime!")
optimal()
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

So, we stop at sqrt(n), because if a number is NOT prime, it must have a divisor before sqrt(n) and
each divisor's counterpart divisor after sqrt(n).
Also, if you think "what if a number after sqrt(n) divides n?" well if it does, then its 
counterpart divisor must be less than sqrt(n), which we must have already checked.
'''