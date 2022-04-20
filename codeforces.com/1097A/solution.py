card_on_the_table = input()
cards_in_hand = input().split()

for c in cards_in_hand:
    if c[0] == card_on_the_table[0] or c[1] == card_on_the_table[1]:
        print('YES')
        break
else:
    print('NO')
