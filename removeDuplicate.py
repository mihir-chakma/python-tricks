# Remove Duplicates from a List in One Line 

original_list = [1, 3, 5, 3, 2, 'ab', 'c', 8, 10, 'ab', 'd', 'c']

filtered_list = list(dict.fromkeys(original_list))

print(filtered_list)
