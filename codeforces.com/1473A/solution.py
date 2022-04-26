for i in range(int(input())):
    number_of_elements, target_value = map(int, input().split())
    array = list(map(int, input().split()))

    if max(array) <= target_value:
        print('YES')
        continue

    array.sort()

    if array[0] + array[1] <= target_value:
        print('YES')
    else:
        print('NO')
