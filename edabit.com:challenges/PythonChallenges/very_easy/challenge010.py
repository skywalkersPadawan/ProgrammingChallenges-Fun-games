"""
ChallengeTitle: Convert Age to Days
Create a function that takes the age in years and returns the age in days.

Examples
calc_age(65) ➞ 23725

calc_age(0) ➞ 0

calc_age(20) ➞ 7300
Notes
Use 365 days as the length of a year for this challenge.
Ignore leap years and days between last birthday and now.
Expect only positive integer inputs.
"""


def calc_age(age):
    return age * 365


# test cases for the function
assert calc_age(10) == 3650, "10 years should be 3650 days."
assert calc_age(0) == 0, "0 years should be 0 days."
assert calc_age(73) == 26645, "73 years should be 26645 days."

# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
