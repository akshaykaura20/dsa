# O(log_{10} N + 1) where N is number of
n = int(input(""))
count = 0

while n != 0:
    count += 1
    n = n // 10 # integer division that leaves the part after decimal

print(count)
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
