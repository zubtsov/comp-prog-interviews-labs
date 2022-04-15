from math import ceil

number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    n = int(input())

    print(int(ceil(n/2)))
