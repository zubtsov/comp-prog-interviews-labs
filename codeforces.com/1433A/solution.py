number_of_test_cases = int(input())

all_boring_numbers = [str(i) * j for i in range(1, 10) for j in range(1, 5)]

for i in range(number_of_test_cases):
    first_boring_apartment_number = input()

    keys_pressed = 0

    for boring_number in all_boring_numbers:
        keys_pressed += len(boring_number)

        if boring_number == first_boring_apartment_number:
            break

    print(keys_pressed)
