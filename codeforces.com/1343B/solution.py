number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    array_length = int(input())
    if (array_length + (array_length / 2 - 1)) % 2 == 0:
        print('NO')
    else:
        print('YES')

        even_numbers = [i for i in range(2, array_length + 1, 2)]

        last_odd_number = int(array_length + (array_length / 2 - 1))
        odd_numbers = [j for j in range(1, array_length - 1, 2)] + [last_odd_number]

        balanced_array = even_numbers + odd_numbers

        print(' '.join(map(str,balanced_array)))
