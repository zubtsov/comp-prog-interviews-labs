number = input()


def is_unlucky_digit(d):
    return d != '4' and d != '7'


all_digits_number = len(number)
unlucky_digits_number = len(list(filter(is_unlucky_digit, number)))
lucky_digits_number = all_digits_number - unlucky_digits_number

if lucky_digits_number == 4 or lucky_digits_number == 7:
    print('YES')
else:
    print('NO')
