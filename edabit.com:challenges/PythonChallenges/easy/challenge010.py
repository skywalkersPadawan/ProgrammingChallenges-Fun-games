"""
ChallengeTitle: End Corona!
Create a function that takes the number of daily average recovered cases recovers, daily average new_cases, current active_cases, and returns the number of days it will take to reach zero cases.

Examples
end_corona(4000, 2000, 77000) ➞ 39

end_corona(3000, 2000, 50699) ➞ 51

end_corona(30000, 25000, 390205) ➞ 79
Notes
The number of people who recover per day recovers will always be greater than daily new_cases.
Be conservative and round up the number of days needed.
"""

import math


def end_corona(recovers, new_cases, active_cases):
    net_decrease = recovers - new_cases
    days = math.ceil(active_cases / net_decrease)
    return days


# test cases for the function
assert end_corona(4000, 2000, 77000) == 39
assert end_corona(3000, 2000, 50699) == 51
assert end_corona(30000, 25000, 390205) == 79
assert end_corona(260000, 255000, 20511691) == 4103


# print message for passing all the test cases for the user
print("\n\nAll the test cases have passed successfully!")
