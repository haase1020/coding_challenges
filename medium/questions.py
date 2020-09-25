# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# def gcd(x, y): return y and gcd(y, x % y) or x
# def lcm(x, y): return x * y / gcd(x, y)


# n = 1
# for i in range(1, 31):
#     n = lcm(n, i)
# print(n)
def sum_square_difference(n):
    numbers = range(1, n+1)
    sum_squares = sum(i**2 for i in numbers)
    square_sum = sum(numbers)**2
    return square_sum - sum_squares


print(sum_square_difference(100))
