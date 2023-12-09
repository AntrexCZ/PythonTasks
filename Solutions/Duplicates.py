"""
Есть список, надо убрать из него повторения, было [1, 3, 4, 6, 4, 2, 2, 2] должно получиться [1, 3, 4, 6, 2]

"""

list1 = [1, 3, 4, 5, 6, 7, 7, 6, 1, 3, 4, 5, 6, 7, 8]

unique_values = []
duplicated_values = []
for i in list1:
    if i not in unique_values:
        unique_values.append(i)
    else:
        duplicated_values.append(i)

print("Duplicates are : ", duplicated_values)
print("Unique values are : ", unique_values)