for i in range(int(input())):
    left, right = map(int, input().split())

    if right / left >= 2:
        print(str(left) + ' ' + str(left * 2))
    else:
        print('-1 -1')
