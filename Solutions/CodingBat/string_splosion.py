"""

Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""
import itertools

x = "Code"

#First Solution
# def string_splosion(str):
#     result = ""
#     for i in range(len(str)):
#         result = result + str[:i + 1]
#     return result

#Second solution
# def string_splosion(str):
#      return "".join([substring for substring in accumulate(str)])

def string_splosion(str):
    xy = itertools.accumulate(str)
    return "".join(list(xy))


print(string_splosion(x))
