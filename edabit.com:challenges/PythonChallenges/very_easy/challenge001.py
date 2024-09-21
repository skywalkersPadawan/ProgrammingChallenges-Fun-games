"""
ChallengeTitle: Return the Sum of Two Numbers
Create a function that takes two numbers as arguments and returns their sum.

Examples
addition(3, 2) ➞ 5

addition(-3, -6) ➞ -9

addition(7, 3) ➞ 10
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
"""


# to return the sum of two numbers in a function and return the result
def addition(a, b):
    return a + b


# test cases for the function
assert addition(2, 3) == 5
assert addition(-3, -6) == -9
assert addition(7, 3) == 10

# print message for passing all the test cases for the user
print("All the test cases have passed successfully!")
