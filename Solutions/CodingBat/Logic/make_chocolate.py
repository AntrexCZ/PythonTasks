"""

We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
"""
x, y, z = (5, 4, 9)


def make_chocolate(small, big, goal):
    big_needed = min(goal // 5, big)
    remaining_small = goal - big_needed * 5

    if remaining_small <= small:
        return remaining_small
    else:
        return -1 if remaining_small > 0 else 0


# Check this task with Vlad, doesn't look correctly., work in progress :)
print(make_chocolate(x, y, z))
