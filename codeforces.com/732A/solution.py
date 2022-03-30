price_of_one_shovel, denomination_of_special_coin = map(int, input().split())

number_of_coins = 0

while True:
    number_of_shovels1 = (10 * number_of_coins + denomination_of_special_coin) / price_of_one_shovel
    number_of_shovels2 = 10 * (number_of_coins + 1) / price_of_one_shovel
    if number_of_shovels1 % 1 == 0:
        print(int(number_of_shovels1))
        break
    elif number_of_shovels2 % 1 == 0:
        print(int(number_of_shovels2))
        break
    else:
        number_of_coins += 1
