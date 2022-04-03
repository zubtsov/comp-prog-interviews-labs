number_of_children = int(input())
talents = list(map(int, input().split()))

programming = list()
math = list()
physics = list()

for i in range(number_of_children):
    student_talent_index = i + 1
    if talents[i] == 1:
        programming.append(student_talent_index)
    elif talents[i] == 2:
        math.append(student_talent_index)
    else:
        physics.append(student_talent_index)

number_of_teams = min(len(programming), len(math), len(physics))

if number_of_teams == 0:
    print(0)
else:
    print(number_of_teams)
    for i in range(number_of_teams):
        print(f'{programming[i]} {math[i]} {physics[i]}')
