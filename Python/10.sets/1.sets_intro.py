
# !! Unqiue Collections
# !! Unordered
# !! Unindexed
# !! Mutable

s = {} # dictinary type
print(type(s))

se = set()
print(type(se))

# non empty set

numbers = {3,2,3,7,3,6,2,6,3,7,4}  #{2, 3, 4, 6, 7} # ?  The appearance of a sorted order in the output is coincidental and not guaranteed.
print(numbers)

se = set("arun",)  # unordered
print(se)
print(type(se))

for num in numbers:
    print(num, end=" ")
