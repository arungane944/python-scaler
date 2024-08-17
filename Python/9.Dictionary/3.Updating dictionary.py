fruit_prices = {'Apple': 1.50, 'Banana': 0.75, 'Cherry': 2.00,
                 'Date': 3.00, 'Elderberry': 5.00, 'Fig': 2.50, 'Grape': 2.20}

# update existing value
fruit_prices["Banana"] = {"small": 5, "large": 10}
fruit_prices["Elderberry"] = 10
print(fruit_prices)

# add new key and value
fruit_prices["Gauva"] = 20
print(fruit_prices)

new_fruits = {'peaches': 1.75, 'plums': 2.25, 'blueberries': 3.00}

fruit_prices.update(new_fruits)
print(fruit_prices)




