"""

Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""
x = [1, 1, 2, 3, 1]


def array123(nums):
    array_to_verify = [1, 2, 3]
    for i in range(len(nums) - 2):
        if nums[i:i + 3] == array_to_verify:
            return True
    return False

print(array123(x))
