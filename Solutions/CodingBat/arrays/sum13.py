"""

Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6
"""
x = [1, 2, 2, 1, 13,2,3]
def sum13(nums):
    for index, number in enumerate(nums):
        if number == 13 and index < len(nums) - 1:
            nums.pop(index+1)
    return sum([number for number in nums if number != 13])

print(sum13(x))

