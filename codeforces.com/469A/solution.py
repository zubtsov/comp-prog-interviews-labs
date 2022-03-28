n = int(input())

little_x_levels = list(map(int, input().split()))
little_y_levels = list(map(int, input().split()))

passed_levels = set(little_x_levels[1:]).union(
    set(little_y_levels[1:])
)

if len(passed_levels) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
