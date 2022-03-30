number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    presence = [False] * 100

    length_of_a = int(input())
    elements_of_a = list(map(int, input().split()))

    min_ai = elements_of_a[0]
    max_ai = elements_of_a[0]

    for ai in elements_of_a:
        if ai > max_ai:
            max_ai = ai
        elif ai < min_ai:
            min_ai = ai

        presence[ai - 1] = True

    if all(presence[min_ai:max_ai]):
        print('YES')
    else:
        print('NO')
