"""

Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
"""
x = [2, 1, 2, 3, 4]
# def count_evens(nums):
#     counter = 0
#     for i in nums:
#         if i % 2 == 0:
#             counter += 1
#     return counter

def count_evens(nums):
    return sum([1 for number in nums if number % 2 == 0])

print(count_evens(x))