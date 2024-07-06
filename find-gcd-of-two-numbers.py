# NUMBER OF APPROACHES: TWO

# O(min(num1, num2))
############################################################################
'''
Algorithm explanation

We start from 1 and go till the min of two numbers as a common divisor can't exceed,
the smaller number of the two, as it has to divide both !
Tip: slightly better approach is to iterate from min(num1, num2) to 1 (backwards) as the difference
between numbers increases, the GCD moves closer to min(num1, num2) but the TC remains same.
'''
def brute_force():
    num1 = int(input())
    num2 = int(input())
    gcd = 1
    for i in range(1, min(num1, num2) + 1):
        if ((num1 % i == 0) and (num2 % i == 0)):
            gcd = i
    print(gcd)
    print(count)
############################################################################
'''
Complexity explanation

The loop runs from 1 to min(num1, num2) hence TC is O(min(num1, num2))
'''

# O(log_{phi}(min(num1, num2))) where `phi` is out of scope for now
############################################################################
'''
Algorithm explanation
`If you cannot solve a bigger problem, solve a smaller problem that has the same answer!`

Euclidean Algorithm:
It is based on the property that gcd(a, b) = gcd(a, b - a), b > a 
Then, let b - a = c, gcd(a, b - a) = gcd(a, c) = gcd(a, c - a), c > a (say)...
You keep on doing this till we reach, gcd (x, x) = gcd(x, 0) which will be x, our gcd.

Why does the gcd remain same after subtraction? Explained in complexity explanation

We are simply subtracting smaller number from bigger number until the smaller becomes bigger. This,
is basically division, where the bigger number after subsequent subtractions is just left as the remainder.
e.g. 10, 34
(10, 34-10) -> (10, 24-10) -> (10, 14-10) or (10, 4) and also, 34 % 10 = 4.

So, the algorithm is reduced to just keep doing:
gcd(a, b) = gcd(smaller, bigger % smaller)
until we reach gcd(x, 0)
'''
def optimal():
    num1 = int(input())
    num2 = int(input())
    while (num1 != 0 and num2 != 0):
        if (num2 > num1):
            num2 = num2 % num1
        else:
            num1 = num1 % num2
    gcd = max(num1, num2) # non zero is gcd
    print(gcd)
optimal()
'''
    Complexity explanation: is out of scope for now.
    Tip: If `%` or repeated `/` are involved- the TC will most probably in terms of logarithm.

    Why does the gcd remain same after subtraction?
    i.e. gcd(a, b) = gcd(a, b - a), b > a 

    Consider number num1 as pile of `num1` or `A` number of stones and similarly 
    num2 as pile of `num2` or `B` number of stones.

    GCD is basically the largest chunk of stones that will divide both piles in some number of parts, 
    say- xa and xb. 
    So, pile A has xa number of GCDs and pile B has xb number of GCDs (largest chunks common for both). 
    => A = g . xa and B = g . xb (Imagine them as bigger balls that make up the pile)

    Now, we remove just one copy of pile A from B. This means:
    => B - A = g . xb - g . xa

    For a moment, let's assume, the largest common chunk size of A and B-A, 
    could maybe get bigger after deletion- to say g' (read: g dash)
    => B - A = g' . x' and A = g' . xa'
    This means, the leftover of pile B is made of g' size chunks with count as x' and 
    pile A is made of g' size chunks with count as xa'.

    But, here's the catch: 
    The deleted pile A from pile B must also be made of g' size chunks with count as xa'. That means:
    => deleted pile A + left over pile B = the original pile B
    => g' . xa' + g' . x' = pile B
    => g' (xa' + x') = pile B
    So, the pile B is made of g' size chunks AND pile A is also made of g' size chunks! 
    A common divisor for A and B!
    What's the largest common divisor for A and B?
    => The GCD(A, B) = g

    Hence, g' = g, the original GCD of A and B!

    
    Watch this video for some intuition https://www.youtube.com/watch?v=Jwf6ncRmhPg
'''