# NUMBER OF APPROACHES: ONE

# O(log_{10} N + 1) where N is the input number
############################################################################
# Algorithm explanation

# In order to reverse the number, we need digits from behind to come first in reversed number.
# Hence, extract digits from behind by using modulus operator. But, how to construct the rev number?

# Lets say we have the number = 1234. When we start reversing it from behind, we are basically doing:
# 4 -> 43 (40 + 3) -> 432 (430 + 2) -> 4321 (4320 + 1)
# Which is simply,
# 4 -> 43 (4*10 + 3) -> 432 (43*10 + 2) -> 4321 (432*10 + 1)

# We keep doing this, until the original number goes zero as we keep removing the extracted digit from
# original number to again extract the next last_digit in next iteration.
# This is done using the integer division operator.
# For e.g. 1234 // 10 = 123 (int) i.e. the integer quotient
def optimal_and_brute_force():
    input_num = int(input(""))
    num_of_digits = 0
    reversed_number = 0

    sign = 1 # preserving sign(+ or - number) for the end
    if input_num < 0:
        sign = -1
    n = abs(input_num)

    while n != 0:
        num_of_digits += 1
        last_digit = n % 10 # extract last digit
        reversed_number = reversed_number * 10 + last_digit
        # remove last digit
        n = n // 10 # integer division that leaves the part after decimal
        # check overflow for 32 bit integers (leetcode)
        if reversed_number > 2**31 - 1 or reversed_number < -2**31:
            return 0
    print(reversed_number * sign)

############################################################################
# Complexity explanation

# Lets consider a k digit number.
# With each iteration, we are simply removing the digits from back of number, hence the time complexity is,
# the number of digits in N i.e. k.

# For a large number N with k number of digits d0, d1, d3, ... dk-2, dk-1:
# N = dk-1 . 10^k-1 + dk-2 . 10^k-2 + dk-3 . 10^k-3 ... d1 . 10^1 + d0 . 10^0 -> k terms, hence our target !

# For practical purposes and large values, the logarithm of a sum of exponentially growing terms,
# can be approximated by the logarithm of the largest term.
# Hence, we approximate:
# log_{10}(N) ≈ log_{10}(dk-1 . 10^k-1) = log_{10}(dk-1) + log_{10}(10^k-1) ≈ k−1 . log_{10}(10) = k-1
# => log_{10}(N) = k-1
# => k = log_{10}(N) + 1
# 
# Hence, number of digits of a number can be approximated to log_{10}(N) + 1, which is the number of times,
# the loop will run, and hence our time complexity is O(log_{10}(N) + 1)#
############################################################################