for t in range(int(input())):
    number_of_rows, number_of_cols, cell_number = map(int, input().split())

    column_number = (cell_number - 1) // number_of_rows
    row_number = (cell_number - 1) % number_of_rows

    print(row_number * number_of_cols + column_number + 1)
