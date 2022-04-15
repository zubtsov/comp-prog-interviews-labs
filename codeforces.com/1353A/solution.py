number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    number_of_elements, sum_of_elements = map(int, input().split())

    if number_of_elements > 2:
        print(sum_of_elements * 2)
    elif number_of_elements == 2:
        print(sum_of_elements)
    else:
        print(0)
