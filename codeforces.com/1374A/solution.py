number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    x, y, n = map(int, input().split())
    m = (n - y) // x
    k = m * x + y
    print(k)
