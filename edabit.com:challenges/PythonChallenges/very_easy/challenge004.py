"""
ChallengeTitle: Area of a Triangle
Write a function that takes the base and height of a triangle and return its area.

Examples
tri_area(3, 2) ➞ 3

tri_area(7, 4) ➞ 14

tri_area(10, 10) ➞ 50
Notes
The area of a triangle is: (base * height) / 2
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""


def tri_area(base, height):
    return (base * height) / 2


# test cases for the function
assert tri_area(3, 2) == 3, "Area of triangle with base 3 and height 2 should be 3."
assert tri_area(5, 4) == 10, "Area of triangle with base 5 and height 4 should be 10."
assert (
    tri_area(10, 10) == 50
), "Area of triangle with base 10 and height 10 should be 50."
assert tri_area(0, 60) == 0, "Area of triangle with base 0 and height 60 should be 0."
assert (
    tri_area(12, 11) == 66
), "Area of triangle with base 12 and height 11 should be 66."


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
