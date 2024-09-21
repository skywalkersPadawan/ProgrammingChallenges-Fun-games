"""
ChallengeTitle: Boolean to String Conversion
Create a function that takes a boolean variable flag and returns it as a string.

Examples
bool_to_string(True) ➞ "True"

bool_to_string(False) ➞ "False"
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""


def squared(a):
    return a * a


# test cases for the function
assert squared(10) == 100, "Expected 100"
assert squared(69) == 4761, "Expected 4761"
assert squared(666) == 443556, "Expected 443556"
assert squared(-21) == 441, "Expected 441"
assert squared(21) == 441, "Expected 441"


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
