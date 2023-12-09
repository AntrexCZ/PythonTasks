"""

Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""

x = ('aabbccdd', 'abbbxxd')


def string_match(a, b):
    count = 0

    for i in range(len(a) - 1):
        for j in range(len(b) - 1):
            print(f"A would be {a[i:i + 2]}")
            print(f"B would be {b[j:j + 2]}")
            print(f"What is the position of A {i} and {i + 1} and B {j} and {j + 1}")

            if (a[i:i + 2] == b[j:j + 2]) and ((i and i + 1) == (j and j + 1)):
                print(f"What is the position of A {i} and B {j}")
                print(f"Yeah, it is the same - {a[i:i + 2]} and {b[j:j + 2]}")
                count += 1
    return count


# Hard task, solved by myself with plenty of debugging), verify with Vlad if it is ok to write like that above.
print(string_match('aabbccdd', 'abbbxxd'))
