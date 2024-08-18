#The id() function in Python returns the "identity" of an object. 
#This identity is unique and constant for the object during its lifetime.
#The identity is an integer that acts as a unique identifier for the object.

a = 10
b = 10

print(id(a))  # Output: 140734564202576 (example value)
print(id(b))  # Output: 140734564202576 (same as above, because a and b point to the same object)

print(id(a)==id(b))

c = []
d = []

print(id(c))  # Output: 140734564202688 (example value)
print(id(d))  # Output: 140734564202704 (different from c, because c and d are different objects)
