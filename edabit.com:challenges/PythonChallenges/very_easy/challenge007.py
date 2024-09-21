"""
ChallengeTitle: Maximum Edge of a Triangle
Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.

Examples
next_edge(8, 10) ➞ 17

next_edge(5, 7) ➞ 11

next_edge(9, 2) ➞ 10
Notes
(side1 + side2) - 1 = maximum range of third edge.
The side lengths of the triangle are positive integers.
Don't forget to return the result.
"""


def next_edge(side1, side2):
    return side1 + side2 - 1


# test cases for the function
assert next_edge(5, 4) == 8, "The maximum third edge for sides 5 and 4 should be 8."
assert next_edge(8, 3) == 10, "The maximum third edge for sides 8 and 3 should be 10."
assert next_edge(7, 9) == 15, "The maximum third edge for sides 7 and 9 should be 15."
assert next_edge(10, 4) == 13, "The maximum third edge for sides 10 and 4 should be 13."
assert next_edge(7, 2) == 8, "The maximum third edge for sides 7 and 2 should be 8."


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
