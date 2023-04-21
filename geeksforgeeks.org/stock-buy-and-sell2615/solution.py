def stockBuySell(price, n):
    is_profitable = False
    trading_day = 0

    while trading_day < (n - 1):
        while (trading_day < (n - 1)) and (price[trading_day] >= price[trading_day + 1]):
            trading_day += 1

        if trading_day >= (n - 1):
            break

        buy_day = trading_day
        trading_day += 1

        while (trading_day < n) and (price[trading_day] >= price[trading_day - 1]):
            trading_day += 1

        sell_day = trading_day - 1

        print('({0} {1})'.format(buy_day, sell_day), end=' ')
        is_profitable = True

    if not is_profitable:
        print('No Profit', end='')
    print()