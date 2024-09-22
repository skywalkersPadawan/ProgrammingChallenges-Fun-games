"""
ChallengeTitle: Find the Discount
Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.

Examples
dis(1500, 50) ➞ 750

dis(89, 20) ➞ 71.2

dis(100, 75) ➞ 25
Notes
Your answer should be rounded to two decimal places.
"""


def dis(price, discount):
    return round(price - (price * discount / 100), 2)


# test cases for the function
assert dis(100, 75) == 25
assert dis(211, 50) == 105.5
assert dis(593, 61) == 231.27
assert dis(1693, 80) == 338.6
assert dis(700, 10) == 630


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
