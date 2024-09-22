"""
ChallengeTitle: Curzon Numbers
In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.

Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.

Examples
is_curzon(5) ➞ True
# 2 ** 5 + 1 = 33
# 2 * 5 + 1 = 11
# 33 is a multiple of 11

is_curzon(10) ➞ False
# 2 ** 10 + 1 = 1025
# 2 * 10 + 1 = 21
# 1025 is not a multiple of 21

is_curzon(14) ➞ True
# 2 ** 14 + 1 = 16385
# 2 * 14 + 1 = 29
# 16385 is a multiple of 29
Notes
N/A
"""


def is_curzon(num):
    # to check if the curzon number formula will work or not
    if (2**num + 1) % (2 * num + 1) == 0:
        return True
    else:
        return False


# test cases for the function
assert is_curzon(5) == True
assert is_curzon(10) == False
assert is_curzon(14) == True
assert is_curzon(86) == True
assert is_curzon(90) == True
assert is_curzon(115) == False
assert is_curzon(120) == False
assert is_curzon(194) == True
assert is_curzon(293) == True


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
