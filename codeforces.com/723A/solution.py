x1, x2, x3 = map(int, input().split())

print(min(
    abs(x3 - x2) + abs(x3 - x1),
    abs(x3 - x2) + abs(x2 - x1),
    abs(x3 - x1) + abs(x2 - x1)
))
