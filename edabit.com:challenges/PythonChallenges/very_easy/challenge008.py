"""
ChallengeTitle: Return the Remainder from Two Numbers
There is a single operator in Python, capable of providing the remainder of a division operation. Two numbers are passed as parameters. The first parameter divided by the second parameter will have a remainder, possibly zero. Return that value.

Examples
remainder(1, 3) ➞ 1

remainder(3, 4) ➞ 3

remainder(5, 5) ➞ 0

remainder(7, 2) ➞ 1
Notes
The tests only use positive integers.
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
"""


def remainder(x, y):
    return x % y


# test cases for the function
assert remainder(7, 2) == 1, "The remainder of 7 divided by 2 should be 1."
assert remainder(3, 4) == 3, "The remainder of 3 divided by 4 should be 3."
assert remainder(5, 5) == 0, "The remainder of 5 divided by 5 should be 0."
assert remainder(1, 3) == 1, "The remainder of 1 divided by 3 should be 1."

# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
