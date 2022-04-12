number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    number_of_gifts = int(input())

    candies_per_gift = list(map(int, input().split()))
    oranges_per_gift = list(map(int, input().split()))

    min_candies = min(candies_per_gift)
    min_oranges = min(oranges_per_gift)

    candies_diff = [c - mc for c, mc in zip(candies_per_gift, [min_candies] * number_of_gifts)]
    oranges_diff = [o - mo for o, mo in zip(oranges_per_gift, [min_oranges] * number_of_gifts)]

    min_number_of_moves = sum([max(cd, od) for cd, od in zip(candies_diff, oranges_diff)])

    print(min_number_of_moves)
