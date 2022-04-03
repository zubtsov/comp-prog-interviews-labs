number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    b_string = input()
    if len(b_string) == 2:
        print(b_string)
    else:
        print(b_string[:2] + b_string[3::2])
