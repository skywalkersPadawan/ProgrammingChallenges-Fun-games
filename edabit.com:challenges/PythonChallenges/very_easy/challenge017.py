"""
ChallengeTitle: Return the First Element in a List
Create a function that takes a list containing only numbers and return the first element.

Examples
get_first_value([1, 2, 3]) ➞ 1

get_first_value([80, 5, 100]) ➞ 80

get_first_value([-500, 0, 50]) ➞ -500
Notes
The first element in a list always has an index of 0.
"""


def get_first_value(number_list):
    return number_list[0]


# test cases for the function
assert get_first_value([1, 2, 3]) == 1, "Expected 1"
assert get_first_value([80, 5, 100]) == 80, "Expected 80"
assert get_first_value([-500, 0, 50]) == -500, "Expected -500"
assert get_first_value([5, 2, 3]) == 5, "Expected 5"
assert get_first_value([75675, 5, 100]) == 75675, "Expected 75675"
assert get_first_value([-52320, 0, 50]) == -52320, "Expected -52320"


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
