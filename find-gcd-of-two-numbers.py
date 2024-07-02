# NUMBER OF APPROACHES: TWO

# O(min(num1, num2))
############################################################################
'''
Algorithm explanation

We start from 1 and go till the min of two numbers as a common divisor can't exceed,
the smaller number of the two, as it has to divide both !
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