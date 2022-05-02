for t in range(int(input())):
    one_burle_coins, two_burles_coins = map(int, input().split())

    if one_burle_coins > 0:
        print(one_burle_coins + 2 * two_burles_coins + 1)
    else:
        print(1)
