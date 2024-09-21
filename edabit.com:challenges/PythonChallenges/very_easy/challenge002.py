"""
ChallengeTitle: Return the Next Number from the Integer Passed
Create a function that takes a number as an argument, increments the number by +1 and returns the result.

Examples
addition(0) ➞ 1

addition(9) ➞ 10

addition(-3) ➞ -2
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""


def addition(num):
    return num + 1


# test cases for the function
assert addition(2) == 3, "2 plus 1 equals 3."
assert addition(-9) == -8, "-9 plus 1 equals -8."
assert addition(0) == 1, "0 plus 1 equals 1."
assert addition(999) == 1000, "999 plus 1 equals 1000."
assert addition(73) == 74, "73 plus 1 equals 74."

# print message for passing all the test cases for the user
print("All the test cases have passed successfully!")
