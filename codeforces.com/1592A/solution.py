import sys

for t in range(int(input())):
    number_of_weapons, initial_enemy_health = map(int, sys.stdin.readline().split())
    damage_values = map(int, sys.stdin.readline().split())

    max1, max2 = next(damage_values), next(damage_values)

    for dv in damage_values:
        if dv > max1 or dv > max2:
            if max1 < max2:
                max1 = dv
            else:
                max2 = dv

    if initial_enemy_health > max1 + max2:
        double_shots = int(initial_enemy_health / (max1 + max2)) * 2
        remainder = initial_enemy_health % (max1 + max2)

        last_shot = 0
        if remainder > max1 and remainder > max2:
            last_shot = 2
        elif remainder != 0:
            last_shot = 1

        total_shots = double_shots + last_shot
        print(total_shots)
    elif initial_enemy_health <= max1 or initial_enemy_health <= max2:
        print(1)
    else:
        print(2)
