"""
ChallengeTitle: Solving Exponential Equations With Logarithms
Create a function that takes a number a and finds the missing exponent x so that a when raised to the power of x is equal to b.

Examples
solve_for_exp(4, 1024) ➞ 5

solve_for_exp(2, 1024) ➞ 10

solve_for_exp(9, 3486784401) ➞ 10
Notes
a is raised to the power of what in order to equal b?
"""

import math


def solve_for_exp(a, b):
    # return a ** (1 / b)
    # there are two ways to solving this problem
    return round(math.log(b, a))


# test cases for the function
assert solve_for_exp(4, 1024) == 5
assert solve_for_exp(2, 1024) == 10
assert solve_for_exp(9, 3486784401) == 10
assert solve_for_exp(4, 4294967296) == 16
assert solve_for_exp(8, 134217728) == 9
assert solve_for_exp(19, 47045881) == 6
assert solve_for_exp(10, 100000000) == 8


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
