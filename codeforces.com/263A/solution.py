matrix_width, matrix_height = 5, 5
for i in range(matrix_height):
    matrix_row = input().split(' ')
    for j in range(matrix_width):
        if matrix_row[j] == '1':
            print(abs(j-2) + abs(i - 2))
            break
