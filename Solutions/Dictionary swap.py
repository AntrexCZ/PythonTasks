"""
Из совсем базовых задач. На входе словарь, нужно поменять ключи и значения местами

На входе {1: "a", 2: "b", 3: "c"}
выход {"a": 1, "b":2, "c": 3}
"""

dict1 = {1: "a", 2: "b", 3: "c"}



# result = dict((v, k) for k, v in dict1.items())
# print(result)

def swap_dict_keys_values(input_dict):
    # Initialize an empty dictionary to store the swapped key-value pairs
    swapped_dict = {}

    # Iterate over each key-value pair in the input dictionary
    for key, value in input_dict.items():
        # Assign the value as the key and the key as the value in the new dictionary
        swapped_dict[value] = key

    # Return the new dictionary with swapped keys and values
    return swapped_dict


result = swap_dict_keys_values(dict1)
print(result)