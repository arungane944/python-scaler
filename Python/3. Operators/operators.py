a = 52
b = 52

print(id(a) , (id(b)), sep=',')

# The is operator in Python is used to compare the identity of two objects. It checks whether two variables point to the same object in memory,
# not just if their values are the same.
print(a is b)