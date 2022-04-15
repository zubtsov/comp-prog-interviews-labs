yakko, wakko = map(int, input().split())

chance = 6 - (max(wakko, yakko) - 1)

if chance == 1:
    print('1/6')
elif chance == 2:
    print('1/3')
elif chance == 3:
    print('1/2')
elif chance == 4:
    print('2/3')
elif chance == 5:
    print('5/6')
else:
    print('1/1')

