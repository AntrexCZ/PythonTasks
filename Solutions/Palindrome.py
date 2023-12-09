"""
дана строка, надо проверить, является ли она палиндромом (читается одинаково с обоих сторон)
"""
x = input()

if x == x[::-1]:
    print("Palindrome")
else:
    print("It is not Polindrome")