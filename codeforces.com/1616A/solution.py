for t in range(int(input())):
    number_of_integers = int(input())
    ints = map(int, input().split())

    counts = {}
    zero_count = 0

    for i in ints:
        if i != 0:
            absi = abs(i)
            counts[absi] = counts.get(absi, 0) + 1
        else:
            zero_count = 1

    print(sum([min(2, v) for v in counts.values()]) + zero_count)
