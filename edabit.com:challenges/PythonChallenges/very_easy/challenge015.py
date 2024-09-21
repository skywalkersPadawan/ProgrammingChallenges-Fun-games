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


def bool_to_string(flag):
    return str(flag)


# test cases for the function
assert bool_to_string(True) == "True", "True should convert to 'True'."
assert bool_to_string(False) == "False", "False should convert to 'False'."

# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
