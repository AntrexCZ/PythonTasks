"""

Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.


has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
"""
x = [1, 2, 1, 2, 2]
def has22(nums):
    a = list(map(str, nums))
    if "22" in "".join(a):
        return True
    return False

print(has22(x))
