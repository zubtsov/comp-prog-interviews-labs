number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    alice, barbara, cerene, polycarp = map(int, input().split())

    missing_coins_to_achieve_equality = (3 * max(alice, barbara, cerene) - (alice + barbara + cerene))
    if polycarp >= missing_coins_to_achieve_equality and (polycarp - missing_coins_to_achieve_equality) % 3 == 0:
        print('YES')
    else:
        print('NO')
