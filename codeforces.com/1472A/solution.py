number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    width, height, target_number_of_sheets = map(int, input().split())

    current_number_of_sheets = 1

    while (width & 1 == 0 or height & 1 == 0) and current_number_of_sheets < target_number_of_sheets:
        if width % 2 == 0:
            width //= 2
            current_number_of_sheets *= 2
        if height % 2 == 0:
            height //= 2
            current_number_of_sheets *= 2

    if current_number_of_sheets >= target_number_of_sheets:
        print('YES')
    else:
        print('NO')
