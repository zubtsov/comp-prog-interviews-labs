number_of_statements = int(input())
value_of_x = 0

for i in range(number_of_statements):
    statement = input()
    if statement[1] == '+':
        value_of_x += 1
    else:
        value_of_x -= 1

print(value_of_x)
