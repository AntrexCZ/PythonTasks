"""

Return the number of times that the string "hi" appears anywhere in the given string.


count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""
x = 'ABChi hi'

def count_hi(a):
    count = 0
    for i in range(len(a)):
        if a[i:i+2] == "hi":
            count += 1
    return count

# from itertools import pairwise
#
#
# def count_hi(a):
#     return sum([1 for i in pairwise(a) if "".join(i) == "hi"])


print(count_hi(x))
