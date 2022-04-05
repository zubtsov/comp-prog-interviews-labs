number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    array_length = int(input())
    array = list(map(int, input().split()))

    even_violations = 0
    odd_violations = 0
    for j in range(array_length):
        if array[j] % 2 != j % 2:
            if j % 2 == 0:
                even_violations += 1
            else:
                odd_violations += 1

    if even_violations == odd_violations:
        print(even_violations)
    else:
        print(-1)
