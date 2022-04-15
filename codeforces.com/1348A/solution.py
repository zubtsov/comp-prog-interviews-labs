number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    number_of_coins = int(input())

    min_difference = (2 ** (number_of_coins / 2 + 1) - 2)

    print(int(min_difference))
