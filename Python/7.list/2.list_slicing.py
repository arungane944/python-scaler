#list mutable
l1 = [1,2,3,4,5]

print(len(l1))

print(l1[::-1])


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 to 5 (5 is not included)
slice1 = numbers[2:6]
print(slice1)  # Output: [2, 3, 4, 5]


# Get elements from the beginning to index 4 (4 is not included)
slice2 = numbers[:4]
print(slice2)  # Output: [0, 1, 2, 3]

# Get elements from index 5 to the end
slice3 = numbers[5:]
print(slice3)  # Output: [5, 6, 7, 8, 9]


# Get the last three elements
slice4 = numbers[-3:]
print(slice4)  # Output: [7, 8, 9]

# Get elements from index 2 to the second last element
slice5 = numbers[2:-1]
print(slice5)  # Output: [2, 3, 4, 5, 6, 7, 8]
