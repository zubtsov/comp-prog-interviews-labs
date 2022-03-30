number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    a, b = map(int, input().split())
    absolute_difference = abs(abs(b) - abs(a))

    if absolute_difference % 10 == 0:
        print(int(absolute_difference / 10))
    else:
        print(int(absolute_difference // 10 + 1))
