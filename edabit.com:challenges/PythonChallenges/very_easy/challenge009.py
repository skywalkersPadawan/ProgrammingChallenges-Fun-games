"""
ChallengeTitle: Return a String as an Integer
Create a function that takes a string and returns it as an integer.

Examples
string_int("6") ➞ 6

string_int("1000") ➞ 1000

string_int("12") ➞ 12
Notes
All numbers will be whole.
All numbers will be positive.
"""


def string_int(txt):
    return int(txt)


# test cases for the function
assert string_int("6") == 6, 'The string "6" should convert to the integer 6.'
assert string_int("2") == 2, 'The string "2" should convert to the integer 2.'
assert string_int("10") == 10, 'The string "10" should convert to the integer 10.'
assert string_int("666") == 666, 'The string "666" should convert to the integer 666.'


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
