# https://edube.org/learn/python-advanced-1/lab-2-1

import copy


class Delicacy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.price = price
        self.weight = weight

    def __str__(self):
        return f'{self.name}; price: {self.price}; weight: {self.weight}'

    def __eq__(self, other):
        if not isinstance(other, Delicacy):
            return False
        return self.name == other.name and self.price == other.price and self.weight == other.weight


delicacies = [Delicacy(name='Lolly Pop', price=0.4, weight=133)]

ref_copy = delicacies
print('ref_copy is delicacies', ref_copy is delicacies)
print()
shallow_copy = delicacies[:]
print('shallow_copy is delicacies', shallow_copy is delicacies)
print('shallow_copy == delicacies', shallow_copy == delicacies)
print('shallow_copy[0] is delicacies[0]', shallow_copy[0] is delicacies[0])
print('shallow_copy[0] == delicacies[0]', shallow_copy[0] == delicacies[0])
print()
deep_copy = copy.deepcopy(delicacies)
print('deep_copy is delicacies', deep_copy is delicacies)
print('deep_copy == delicacies', deep_copy == delicacies)
print('deep_copy[0] is delicacies[0]', deep_copy[0] is delicacies[0])
print('deep_copy[0] == delicacies[0]', deep_copy[0] == delicacies[0])
