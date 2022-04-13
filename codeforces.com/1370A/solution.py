number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    n = int(input())

    if n > 3:
        print(n // 2)
    else:
        print(1)
