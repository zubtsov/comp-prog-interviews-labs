table_size = int(input())

values = [[0] * table_size for i in range(table_size)]
# TODO: is there an analytical solution? not brute force
for i in range(table_size):
    values[0][i] = 1
    values[i][0] = 1

for row in range(1, table_size):
    for col in range(1, table_size):
        values[row][col] = values[row][col - 1] + values[row - 1][col]

print(values[table_size - 1][table_size - 1])
