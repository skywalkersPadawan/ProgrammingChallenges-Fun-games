"""
ChallengeTitle: Radians to Degrees
Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.

Examples
radians_to_degrees(1) ➞ 57.3

radians_to_degrees(20) ➞ 1145.9

radians_to_degrees(50) ➞ 2864.8
Notes
The number π can be loaded from the math module with from math import pi.
"""

import math


def radians_to_degrees(radians):
    return round(radians * (180 / math.pi), 1)


# test cases for the function
assert radians_to_degrees(1) == 57.3
assert radians_to_degrees(5) == 286.5
assert radians_to_degrees(7) == 401.1
assert radians_to_degrees(60) == 3437.7
assert radians_to_degrees(100) == 5729.6
assert radians_to_degrees(180) == 10313.2


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
