calories_per_click = dict([(str(index + 1), int(calories)) for index, calories in enumerate(input().split())])
total_calories_burned = sum([calories_per_click[c] for c in input()])

print(total_calories_burned)
