# Loop through numbers 1 to 10
for i in range(1, 11):
    if i == 3:
        continue  # Skip the rest of the loop when i is 3
    if i == 7:
        break  # Exit the loop when i is 7
    print(i)
