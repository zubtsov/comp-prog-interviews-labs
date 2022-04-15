rows, columns = map(int, input().split())

for i in range(rows):
    for color in input().split():
        if color != 'B' and color != 'G' and color != 'W':
            print('#Color')
            break
    else:
        continue
    break
else:
    print('#Black&White')
