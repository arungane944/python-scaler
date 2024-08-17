fruit_prices = {'Apple': 1.50, 'Banana': 0.75, 'Cherry': 2.00, 'Date': 3.00, 'Elderberry': 5.00, 'Fig': 2.50, 'Grape': 2.20}

print(fruit_prices.get("Apple"))
print(fruit_prices["Apple"])
#print(fruit_prices["Pineapple"]) # to avoid this error use get()


print(fruit_prices.get("Pineapple"))
print(fruit_prices.get("Pineapple", "Not available"))
