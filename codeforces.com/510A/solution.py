rows, columns = map(int, input().split())

snake_part = '#'
empty_cell = '.'

for r in range(1, rows + 1):
    if r % 2 == 1:
        print(snake_part * columns)
    elif r % 4 == 0:
        print(snake_part + empty_cell * (columns - 1))
    else:
        print(empty_cell * (columns - 1) + snake_part)
