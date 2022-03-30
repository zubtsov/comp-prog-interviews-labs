number_of_test_cases = int(input())
# TODO: reduce execution time
for i in range(number_of_test_cases):
    number = input()
    number_length = len(number)

    summands = ''
    summands_number = 0

    start_pos = 0
    end_pos = 1
    while end_pos <= number_length:
        if end_pos == number_length or number[end_pos] != '0':
            summands += number[start_pos:end_pos].ljust(number_length - start_pos, '0')
            summands_number += 1

            start_pos = end_pos
            end_pos += 1

            if end_pos < number_length + 1:
                summands += ' '
        else:
            end_pos += 1

    print(summands_number)
    print(summands)
