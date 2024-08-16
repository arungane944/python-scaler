#list mutable
l1 = [1,2,3,4,5]

print(len(l1))
print(l1)
print(id(l1))

l1[0]=5
print(l1)
print(id(l1))

for num in l1:
    print(num)