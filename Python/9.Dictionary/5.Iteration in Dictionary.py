fruit_prices = {'Apple': 1.50, 'Banana': 0.75, 'Cherry': 2.00,
                 'Date': 3.00, 'Elderberry': 5.00, 'Fig': 2.50, 'Grape': 2.20}

for key in fruit_prices:
    print(key, fruit_prices[key])


# !! inbuild methods

for key,value in fruit_prices.items():
    print(key,value)

#methods:
    
fruit_prices.keys()
fruit_prices.values()