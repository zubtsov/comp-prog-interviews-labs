friends_house_coordinate = int(input())

number_of_steps = 0

for step_size in range(5, 0, -1):
    current_size_steps = friends_house_coordinate // step_size
    number_of_steps += current_size_steps
    friends_house_coordinate -= current_size_steps * step_size

print(number_of_steps)
