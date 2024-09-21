"""
ChallengeTitle: Convert Minutes into Seconds
Write a function that takes an integer minutes and converts it to seconds.

Examples
convert(5) ➞ 300

convert(3) ➞ 180

convert(2) ➞ 120
Notes
Don't forget to return the result.
If you get stuck on a challenge, find help in the Resources tab.
If you're really stuck, unlock solutions in the Solutions tab.
"""


def convert(minutes):
    return minutes * 60  #  to convert minutes to seconds


# test cases for the function
assert convert(6) == 360, "6 minutes should be 360 seconds."
assert convert(4) == 240, "4 minutes should be 240 seconds."
assert convert(8) == 480, "8 minutes should be 480 seconds."
assert convert(60) == 3600, "60 minutes should be 3600 seconds."

# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
