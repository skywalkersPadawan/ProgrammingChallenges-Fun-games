"""
ChallengeTitle: Find the Perimeter of a Rectangle
Create a function that takes length and width and finds the perimeter of a rectangle.

Examples
find_perimeter(6, 7) ➞ 26

find_perimeter(20, 10) ➞ 60

find_perimeter(2, 9) ➞ 22
Notes
Don't forget to return the result.
If you're stuck, find help in the Resources tab.
If you're really stuck, find solutions in the Solutions tab.
"""


def find_perimeter(length, width):
    return (length * 2) + (width * 2)


# test cases for the function
assert (
    find_perimeter(6, 7) == 26
), "The perimeter for length 6 and width 7 should be 26."
assert (
    find_perimeter(20, 10) == 60
), "The perimeter for length 20 and width 10 should be 60."
assert (
    find_perimeter(2, 9) == 22
), "The perimeter for length 2 and width 9 should be 22."


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
