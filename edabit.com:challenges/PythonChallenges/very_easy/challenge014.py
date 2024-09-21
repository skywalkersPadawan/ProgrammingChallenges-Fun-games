"""
ChallengeTitle: To the Power of _____
Create a function that takes a base number and an exponent number and returns the calculation.

Examples
calculate_exponent(5, 5) ➞ 3125

calculate_exponent(10, 10) ➞ 10000000000

calculate_exponent(3, 3) ➞ 27
Notes
All test inputs will be positive integers.
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""


def calculate_exponent(num, exp):
    return num**exp


# test cases for the function
assert calculate_exponent(5, 5) == 3125, "5 raised to the power of 5 should be 3125."
assert calculate_exponent(3, 3) == 27, "3 raised to the power of 3 should be 27."
assert (
    calculate_exponent(10, 10) == 10000000000
), "10 raised to the power of 10 should be 10000000000."

# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
