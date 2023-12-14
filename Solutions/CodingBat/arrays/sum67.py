"""
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7
(every 6 will be followed by at least one 7). Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""
x = [1, 6, 2, 2, 7, 1, 6, 99, 99, 7, 2]


def sum67(nums):
    exclude_section = False
    sum_nums = 0
    for number in nums:
        if number == 6:
            exclude_section = True
        elif number == 7 and exclude_section:
            exclude_section = False
        elif not exclude_section:
            sum_nums += number
    return sum_nums

#Was super hard tasks, until I got flags, otherwise idk how to solve it
print(sum67(x))
