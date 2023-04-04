nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_list = []

# Nested for loop to access the inner list
for items in nested_list:
    for num in items:
        #Create a list of numbers wanted
        if num in [3, 5, 9]:
            # Checking if number already exists before appending
            if num not in new_list:
                new_list.append(num)

print(new_list)
