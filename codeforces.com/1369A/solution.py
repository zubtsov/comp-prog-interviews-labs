for i in range(int(input())):
    number_of_sides = int(input())  # >= 3

    if number_of_sides % 4 == 0:
        print('YES')
    else:
        print('NO')
