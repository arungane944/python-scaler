
# !! 1. Stores data in key and value pair
# !! 2. Ordered datastructure
# !! 3. Doesnot store indexing
# !! 4. Data can be accessed with key

d = {}
print(type(d))

# or

d1 = dict()
print(type(d1))

# non empty dict

fruits = {
    "Apple" : 120,
    "mongo" : 23,
    "pineapple" : 56
    }

print(fruits)

 # Zip Method

name = ["Apple","Mongo","Pineapple"]
price = [120,23,56]
print(type(name), type(price))

good_fruits = dict(zip(name,price))  # !! very important

print(good_fruits)


# length

print(len(good_fruits))