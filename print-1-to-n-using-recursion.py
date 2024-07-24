# NUMBER OF APPROACHES: ONE 

# O(n)
############################################################################
'''
Algorithm explanation

When you pass n to function fn(n), it checks if n == 0.
Then you call the fn itself for n-1 value fn(n - 1). Why?
We are doing this, because first we want to-
reduce the 'n' to '1' (n, n - 1, n-1 - 1, ... 1) and when it does, we print it.
Hence, when the fn at top of call stack fn(0), checks that n == 0, returns, meaning fn(0) pops.
The next top fn in call stack fn(1), which was waiting before, finally prints 1. 
Then next top fn in call stack fn(2), which was waiting before, finally prints 2. 
This process now goes on from fn(1), fn(2), fn(3)... to fn(n).

Visualise in complexity explanation
'''
def print_1_to_n(n):
    if(n == 0):
        return
    print_1_to_n(n - 1)
    print(n, end=" ")
    
def optimal():
    n = int(input(""))
    print_1_to_n(n)
optimal()
############################################################################
'''
Complexity explanation

Since we are calling a function n times- TC: O(n)

Visualize call stack for n = 5
                                        fn(0)
                                fn(1)   fn(1)
                        fn(2)   fn(2)   fn(2)
                fn(3)   fn(3)   fn(3)   fn(3)
        fn(4)   fn(4)   fn(4)   fn(4)   fn(4)
fn(5)   fn(5)   fn(5)   fn(5)   fn(5)   fn(5)

Popping starts, i.e. n == 0 is true, hence fn(0) returns to fn(1) and executes the last statement in fn(1).
And this happens for all below fn calls

fn(1) -> 1
fn(2)           fn(2) -> 2
fn(3)           fn(3)           fn(3) -> 3
fn(4)           fn(4)           fn(4)           fn(4) -> 4
fn(5)           fn(5)           fn(5)           fn(5)           fn(5) -> 5
'''