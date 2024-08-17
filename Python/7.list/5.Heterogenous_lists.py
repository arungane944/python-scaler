heterogeneous_list = [
    1,                   # An integer
    3.14,                # A floating-point number
    'Python',            # A string
    [5, 6, 7],           # A nested list
    {'name': 'Alice'},   # A dictionary
    (8, 9),              # A tuple
    False                # A boolean
]

# Print the entire list
print("Heterogeneous List:")
print(heterogeneous_list)

# Iterate over the list and print each element along with its type
print("\nElement Types:")
for element in heterogeneous_list:
    print(f'Element: {element}, Type: {type(element)}')