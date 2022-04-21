for i in range(int(input())):
    array_length = int(input())
    elements = map(int, input().split())
    elements_counts = {}

    for e in elements:
        elements_counts[e] = elements_counts.get(e, 0) + 1
        if elements_counts[e] >= 3:
            print(e)
            break
    else:
        print(-1)
