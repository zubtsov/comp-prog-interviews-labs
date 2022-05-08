def is_between(end1, end2, point):
    return end1 < point < end2 or end1 > point > end2


for t in range(int(input())):
    input()

    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xf, yf = map(int, input().split())

    shortest_path_length = abs(xa-xb) + abs(ya-yb)

    if (xa == xb == xf and is_between(ya, yb, yf)) or (ya == yb == yf and is_between(xa, xb, xf)):
        shortest_path_length += 2

    print(shortest_path_length)
