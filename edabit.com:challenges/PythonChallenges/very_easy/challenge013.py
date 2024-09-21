"""
ChallengeTitle: Sum of Polygon Angles
Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).

Examples
sum_polygon(3) ➞ 180

sum_polygon(4) ➞ 360

sum_polygon(6) ➞ 720
Notes
n will always be greater than 2.
The formula (n - 2) x 180 gives the sum of all the measures of the angles of an n-sided polygon.
"""


def sum_polygon(n):
    return (n - 2) * 180


# test cases for the function
from random import randint

for i in range(3, randint(50, 1000)):
    assert sum_polygon(i) == (i - 2) * 180, "failed for n = {}".format(i)


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
