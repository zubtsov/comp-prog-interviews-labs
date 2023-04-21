def stockBuySell(price, n):
    buy_sell_deals = []

    trading_day = 0

    while trading_day < n - 1:
        while not (
                (trading_day == 0 and price[trading_day] < price[trading_day + 1]) or
                (trading_day == n - 1 and price[trading_day - 1] > price[trading_day]) or
                (price[trading_day - 1] > price[trading_day] and
                 price[trading_day] < price[trading_day + 1])
        ):
            trading_day += 1
        last_local_minimum_day = trading_day

        if trading_day >= n - 1:
            break

        while not (
                (trading_day == 0 and price[trading_day] > price[trading_day + 1]) or
                (trading_day == n - 1 and price[trading_day - 1] < price[trading_day]) or
                (price[trading_day - 1] < price[trading_day] and
                 price[trading_day] > price[trading_day + 1])
        ):
            trading_day += 1
        last_local_maximum_day = trading_day

        delta = price[last_local_maximum_day] - price[last_local_minimum_day]
        if delta > 0:
            buy_sell_deals.append((last_local_minimum_day, last_local_maximum_day))

        trading_day += 1

    if buy_sell_deals:
        print(' '.join(map(lambda t: '({0} {1})'.format(t[0], t[1]), buy_sell_deals)))
    else:
        print('No Profit')
