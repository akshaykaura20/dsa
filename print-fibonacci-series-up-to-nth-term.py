# NUMBER OF APPROACHES: ONE 

# This program prints the nth fibonacci term, NOT  the entire sequence.
# TC: O(2^n), SC: O(n)
############################################################################
'''
Algorithm explanation

fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
until n is either 0 or 1 which means the first two terms of fibonacci sequence:
0 1 1 2 3 5...

Visualise in complexity explanation
'''
def rec_fib(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return rec_fib(n - 1) + rec_fib(n - 2)

def optimal():
    n = int(input(""))
    ans = rec_fib(n)
    print(ans)
optimal()
############################################################################
'''
Complexity explanation

Since one fn call, leads to two fn calls (binary tree), and this happens from n to 1 (n times),
2 => 2^2 => (2^2)^2...
=> TC: O(2^n)

And since the max depth of call stack (or binary tree) is n, 
=> SC: O(n)

Visualize call stack for n = 5
            rec_fib(5)
           /         \
     rec_fib(4)      rec_fib(3)
       /      \        /      \
 rec_fib(3) rec_fib(2) rec_fib(2) rec_fib(1)
    /     \      /    \      /    \
rec_fib(2) rec_fib(1) rec_fib(1) rec_fib(0) rec_fib(1) rec_fib(0)
   /    \
rec_fib(1) rec_fib(0)

'''