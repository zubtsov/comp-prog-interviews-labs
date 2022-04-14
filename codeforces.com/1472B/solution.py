number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    number_of_candies = int(input())

    one_gram_candies_number = 0
    two_grams_candies_number = 0

    for weight in map(int, input().split()):
        if weight == 1:
            one_gram_candies_number += 1
        else:
            two_grams_candies_number += 1

    if one_gram_candies_number == 0 and two_grams_candies_number % 2 == 0:
        print('YES')
    elif one_gram_candies_number != 0 and one_gram_candies_number % 2 == 0:
        print('YES')
    else:
        print('NO')
