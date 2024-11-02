# NUMBER OF APPROACHES: TWO (Recursive and Iterative)

# TC: O(n), SC: O(1)
############################################################################
'''
Algorithm explanation

factorial(n) = n * factorial(n - 1)

Visualise in complexity explanation
'''
def rec_factorial(num):
    if(num == 1 or num == 0):
        return 1
    return num * rec_factorial(num - 1)

def optimal_rec():
    num = list(map(int, input("").split(" ")))
    ans = rec_factorial(num[0])
    print(ans)
optimal_rec()
############################################################################
'''
Complexity explanation

Visualize call stack for n = 5
                                                                                  fn(1) -> return 1
                                                     fn(2) -> 2 * fn(1)           fn(2) -> 2 * fn(1)
                                                     fn(3) -> 2 * fn(2)           fn(3) -> 2 * fn(1)
                        fn(4) -> 4 * fn(3)           fn(4) -> 4 * fn(3)           fn(4) -> 4 * fn(3)
fn(5) -> 5 * fn(4)      fn(5) -> 5 * fn(4)           fn(5) -> 5 * fn(4)           fn(5) -> 5 * fn(4)

Popping starts, i.e. n == 1 is true, hence fn(1) returns (1) to fn(2), which returns 2 * (1),
control goes to fn(3) and ...

fn(1) -> 1
fn(2)           fn(2) -> 2 * (1)
fn(3)           fn(3)           fn(3) -> 3 * (2)
fn(4)           fn(4)           fn(4)           fn(4) -> 4 * (6)
fn(5)           fn(5)           fn(5)           fn(5)           fn(5) -> 5 * (24) = 120

Since we are calling a function n times- TC: O(n)
'''


# APPROACH #2: ITERATIVE
# TC: O(n), SC: O(1)
############################################################################
'''
Algorithm explanation

As factorial(n) = n * (n - 1) * (n - 2) ... 1
or,
factorial(n) = 1 * 2 * 3 ... (n)

hence we can use a loop to calculate this product.
But we must use the preceding product, and update the current value of factorial,
by just multiplying it with next one,
i.e. current_factorial = current_factorial * i
for eg

fn(4) will be done this way:
current_factorial = 1
current_factorial = 1 * 2
current_factorial = 2 * 3
current_factorial = 6 * 4 = 24

As the loop runs from 1 to n => TC: O(n)
'''