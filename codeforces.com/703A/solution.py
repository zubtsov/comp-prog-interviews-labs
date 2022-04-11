game_rounds_number = int(input())

mishka_total_wins = 0
chris_total_wins = 0

for i in range(game_rounds_number):
    mishka_dice_value, chris_dice_value = map(int, input().split())
    if mishka_dice_value > chris_dice_value:
        mishka_total_wins += 1
    elif mishka_dice_value < chris_dice_value:
        chris_total_wins += 1

if mishka_total_wins > chris_total_wins:
    print('Mishka')
elif mishka_total_wins == chris_total_wins:
    print('Friendship is magic!^^')
else:
    print('Chris')
