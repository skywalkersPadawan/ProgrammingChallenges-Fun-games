"""
ChallengeTitle: Buggy Code (Part 1)
Fix the code in the code tab to pass this challenge (only syntax errors). Look at the examples below to get an idea of what the function should do.

Examples
cubes(3) ➞ 27

cubes(5) ➞ 125

cubes(10) ➞ 1000
Notes
READ EVERY WORD CAREFULLY, CHARACTER BY CHARACTER!
Don't overthink this challenge; it's not supposed to be hard.
"""


def cubes(a):
    return a**3


# test cases for the function
assert cubes(2) == 8, "2 cubed should be 8."
assert cubes(3) == 27, "3 cubed should be 27."
assert cubes(4) == 64, "4 cubed should be 64."
assert cubes(5) == 125, "5 cubed should be 125."
assert cubes(10) == 1000, "10 cubed should be 1000."


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
