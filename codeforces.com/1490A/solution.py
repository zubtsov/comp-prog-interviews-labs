from math import ceil, log2

for t in range(int(input())):
    array_len = int(input())
    array = list(map(int, input().split()))

    numbers_to_insert = 0

    for i in range(1, array_len):

        ratio = max(array[i - 1], array[i]) / min(array[i - 1], array[i])
        if ratio > 2:
            numbers_to_insert += ceil(log2(ratio)) - 1

    print(numbers_to_insert)
