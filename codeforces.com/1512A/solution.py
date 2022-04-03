number_of_cases = int(input())

for i in range(number_of_cases):
    array_length = int(input())
    array = list(map(int, input().split()))

    for j in range(2, len(array)):
        if array[j - 2] != array[j - 1] and array[j - 2] != array[j]:
            print(j - 1)
            break
        elif array[j - 1] != array[j - 2] and array[j - 1] != array[j]:
            print(j)
            break
        elif array[j - 2] != array[j] and array[j - 1] != array[j]:
            print(j + 1)
            break
