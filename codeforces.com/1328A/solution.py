from math import ceil

number_of_cases = int(input())

for i in range(number_of_cases):
    a, b = map(int, input().split())
    print(ceil(a / b) * b - a)
