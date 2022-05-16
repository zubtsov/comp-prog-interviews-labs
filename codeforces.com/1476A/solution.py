from math import ceil

for t in range(int(input())):
    n, k = map(int, input().split())

    max_elem = ceil((ceil(n / k) * k) / n)
    print(max_elem)
