"""
ChallengeTitle: Circle or Square
Given the radius of a circle and the area of a square, return True if the circumference of the circle is greater than the square's perimeter and False if the square's perimeter is greater than the circumference of the circle.

Examples
circle_or_square(16, 625) ➞ True

circle_or_square(5, 100) ➞ False

circle_or_square(8, 144) ➞ True
Notes
You can use Pi to 2 decimal places (3.14).
Circumference of a circle equals 2 * Pi * radius.
To find the perimeter of a square using its area, find the square root of area (to get side length) and multiply that by 4.
"""


def circle_or_square(rad, area):
    circumference_of_circle = 2 * 3.14 * rad
    square_sideLength = area**0.5
    perimeter_of_square = 4 * square_sideLength

    if circumference_of_circle > perimeter_of_square:
        return True
    else:
        return False


# test cases for the function
assert circle_or_square(16, 625) == True
assert circle_or_square(8, 144) == True
assert circle_or_square(15, 400) == True
assert circle_or_square(5, 100) == False
assert circle_or_square(18, 900) == False
assert circle_or_square(1, 4) == False


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
