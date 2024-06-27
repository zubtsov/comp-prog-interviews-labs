# https://edube.org/learn/python-advanced-1/lab-1-1

import copy

warehouse = list()
warehouse.append({'name': 'Lolly Pop', 'price': 0.4, 'weight': 133})
warehouse.append({'name': 'Licorice', 'price': 0.1, 'weight': 251})
warehouse.append({'name': 'Chocolate', 'price': 1, 'weight': 601})
warehouse.append({'name': 'Sours', 'price': 0.01, 'weight': 513})
warehouse.append({'name': 'Hard candies', 'price': 0.3, 'weight': 433})

print('Source list of candies')
for item in warehouse:
    print(item)

print("*" * 18)
print("Price proposal")
reduced_prices = copy.deepcopy(warehouse)
for item in reduced_prices:
    if item['weight'] > 300:
        item['price'] *= 0.8
    print(item)
