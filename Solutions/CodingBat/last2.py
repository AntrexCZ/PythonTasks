"""
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the
last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""

x = "heldlo world"


def last2(str):
    count = 0
    lt2 = str[-2::]
    for i in range(len(str) - 2):
        step = str[i:i + 2]
        if lt2 == step:
            count += 1
    return count


# This one was hard to solve
print(last2(x))
