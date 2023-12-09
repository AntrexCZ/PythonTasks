"""

Given an array of ints, return True if one of the first 4 elements in the array is a 9.
The array length may be less than 4.


array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""

x = [1, 2, 9, 3, 4]

def array_front9(nums):
    count = 0
    for i in nums[:3]:
        if i == 9:
            count += 1
            return True
    if count < 1:
        return False


# Should be adjusted and refactored, code doesn't look pretty
print(array_front9(x))