for t in range(int(input())):
    a, b, threshold = map(int, input().split())

    steps = 0
    while a <= threshold and b <= threshold:
        if a < b:
            a += b
        else:
            b += a
        steps += 1

    print(steps)
