import random


class Apple:
    _processed_apples_number = 0
    _processed_apples_weight = 0

    def __init__(self):
        new_apple_weight = random.uniform(0.1, 0.5)  # 0.2 is too high

        if Apple._processed_apples_number >= 1000:
            raise Exception('Too many apples')
        if Apple._processed_apples_weight + new_apple_weight >= 300:
            raise Exception('Total apples weight exceeds limit')

        Apple._processed_apples_number += 1
        Apple._processed_apples_weight += new_apple_weight


try:
    while True:
        Apple()
except Exception as e:
    print(e)
    print('Total apples created:',
          Apple._processed_apples_number,
          'Total weight:',
          Apple._processed_apples_weight)
