"""
There are 2 strings, compare them :) aaa & aaa = True, if there is something else, print False
"""

input_string = input().split(",")

if input_string[0] == input_string[1] or input_string[0][::-1] == input_string[1][::-1]:
    print("Strings are equals")
else:
    print("Strings are not equal")