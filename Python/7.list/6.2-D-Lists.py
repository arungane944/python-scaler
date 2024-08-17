# Create a 2D list (a list of lists)
matrix = [
    [1, 2, 3],    # First row
    [4, 5, 6],    # Second row
    [7, 8, 9]     # Third row
]

# Print the entire 2D list
print("2D List (Matrix):")
for row in matrix:
    print(row)

# Accessing elements
print("\nAccessing Specific Elements:")
print("Element at (0, 0):", matrix[0][0])  # First row, first column
print("Element at (1, 2):", matrix[1][2])  # Second row, third column
print("Element at (2, 1):", matrix[2][1])  # Third row, second column

# iteration

for list in matrix:
    for number in list:
        print(number, end=" ")
    print()