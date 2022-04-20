for i in range(int(input())):
    a, b, c = map(int, input().split())

    mi = min(a, b)
    ma = max(a, b)
    half_circle_people = (ma - mi)
    full_circle_people = 2 * half_circle_people

    if ma > half_circle_people * 2 or c > full_circle_people:
        print(-1)
    else:
        print((c - half_circle_people - 1) % full_circle_people + 1)
