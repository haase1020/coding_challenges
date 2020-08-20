# the fibonacci sequences is defined as follows: the first number of the sequence is 0,
# 2nd 1, and nth is the sum of the (n-1)_th and (n-2)th numbers Write a function tat takes an
# integer n and returns the nth Fib num. For this question, the 1st fib num is F0:
# so getNthFib(1) is equal to F0, getNthFib(2) is equal to F1, etc.
# 0,1,1,2,3,5,8,13,21,34  fib(n) = fib(n-1) + fib(n-2) for n >2
# recursive solution is time complexity 0(2^n) and space is 0(n) because use fn call stack
# recursive solution with memoizing is much better: 0(n) time and space
# iterative solution is best: 0(n) time space 0(1)

# naive recursive
# def getNthFib(n):
#     if n == 2:
#         return 1
#     elif n == 1:
#         return 0
#     else:
#         return getNthFib(n-1) + getNthFib(n-2)


# # better recursive
# This solution uses memoization, which basically creates a cache to store data
# if n is in memoize, return memoize[n]
# def getNthFib(n, memoize={1: 0, 2: 1}):  # holds the base cases
#     if n in memoize:
#         return memoize[n]
#     else:
#         memoize[n] = getNthFib(n - 1, memoize) + getNthFib(n - 2, memoize)
#         return memoize[n]

# iterative - really good solution
# store last two fib numbers in a list
# time complexity: 0(n)   space complexity: 0(1) -> just stores two numbers at a time


def getNthFib(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]


print(getNthFib(20))
