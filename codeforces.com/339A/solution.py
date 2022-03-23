from functools import reduce

list = list(input().split('+'))
list.sort()
print(reduce(lambda a, b: a + '+' + b, list))
