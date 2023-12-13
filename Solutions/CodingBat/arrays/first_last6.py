"""

Given an array of ints, return True if 6 appears as either the first or last element in the array.
The array will be length 1 or more.


first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
"""
x = [1, 2, 6]
def first_last6(nums):
    numb_str = "".join(map(str, nums))
    return numb_str.startswith("6") or numb_str.endswith("6")

print(first_last6(x))