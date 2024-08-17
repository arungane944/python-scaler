# write python program to print event numbers from the list

input = [1,2,3,4,5,6,7,8,9]

output = set()

find_even_numbers = lambda number: output.add(number) if number % 2 == 0 else None

for number in input:
    find_even_numbers(number)

print(list(output))