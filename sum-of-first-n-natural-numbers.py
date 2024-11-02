# NUMBER OF APPROACHES: ONE 

# O(n)
############################################################################
'''
Algorithm explanation

When you pass n to function fn(n), it checks if n == 0.
If not, then we add the current value of n with value returned by fn(n-1)
We are doing this, because first we want to-
reduce the 'n' to '1' i.e. (n, n - 1, n-1 - 1, ... 1, 0)
Hence, as we go up the call stack, we keep calling a lesser n value fn(n - 1).
And when the fn at top of call stack fn(0), checks that n == 0, returns, meaning fn(0) pops.
The next top fn in call stack fn(1), which was waiting before, finally just simply completes itself,
with nothing left to do, and control is returned to fn(2)
Then next top fn in call stack fn(2), which was waiting before, follows the same.
This process now goes on from fn(1), fn(2), fn(3)... to fn(n).

Visualise in complexity explanation
'''
def sum_n_to_1(n):
    if(n == 0):
        return 0
    print(n, end=" ")
    return n + sum_n_to_1(n - 1)

def optimal():
    n = int(input(""))
    ans = sum_n_to_1(n)
    print(ans)
optimal()
############################################################################
'''
Complexity explanation

Since we are calling a function n times- TC: O(n)

Visualize call stack for n = 5
                                                                                fn(0) -> return
                                                                fn(1) -> 1      fn(1)
                                                fn(2) -> 2      fn(2)           fn(2)
                                fn(3) -> 3      fn(3)           fn(3)           fn(3)
                fn(4) -> 4      fn(4)           fn(4)           fn(4)           fn(4)
fn(5) -> 5      fn(5)           fn(5)           fn(5)           fn(5)           fn(5)

Popping starts, i.e. n == 0 is true, hence fn(0) returns to fn(1), with nothing in fn(1) left to do.
And this happens for all below fn calls

fn(1)
fn(2)           fn(2)
fn(3)           fn(3)           fn(3)
fn(4)           fn(4)           fn(4)           fn(4)
fn(5)           fn(5)           fn(5)           fn(5)           fn(5)
'''