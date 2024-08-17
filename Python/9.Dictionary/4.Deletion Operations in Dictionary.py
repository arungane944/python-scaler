fruit_prices = {'Apple': 1.50, 'Banana': 0.75, 'Cherry': 2.00,
                 'Date': 3.00, 'Elderberry': 5.00, 'Fig': 2.50, 'Grape': 2.20}

# citizenship check

print("apple" in fruit_prices)

# delete objects

# pop

fruit_prices.pop("Apple")
print(fruit_prices)


# pop item

fruit_prices.popitem() # deletes last item
print(fruit_prices)

# del

del fruit_prices # deleting from computer memory

print(fruit_prices)