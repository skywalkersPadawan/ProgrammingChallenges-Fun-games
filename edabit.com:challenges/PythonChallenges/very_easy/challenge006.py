"""
ChallengeTitle: Convert Hours into Seconds
Write a function that converts hours into seconds.

Examples
how_many_seconds(2) ➞ 7200

how_many_seconds(10) ➞ 36000

how_many_seconds(24) ➞ 86400
Notes
60 seconds in a minute, 60 minutes in an hour
Don't forget to return your answer.
"""


def how_many_seconds(hours):
    return hours * 3600


# test cases for the function
assert how_many_seconds(2) == 7200, "2 hours should be 7200 seconds."
assert how_many_seconds(10) == 36000, "10 hours should be 36000 seconds."
assert how_many_seconds(24) == 86400, "24 hours should be 86400 seconds."
assert how_many_seconds(36) == 129600, "36 hours should be 129600 seconds."


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
