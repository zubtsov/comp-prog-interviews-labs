apartments_on_first_floor = 2

for i in range(int(input())):
    apartment_number, number_of_apartments_per_floor = map(int, input().split())

    if apartment_number <= 2:
        print(1)
    elif apartment_number <= number_of_apartments_per_floor + 2:
        print(2)
    else:
        for floor in range(3, 1000):
            if ((floor - 2) * number_of_apartments_per_floor + 2 + 1) <= apartment_number <= (
                    (floor - 1) * number_of_apartments_per_floor + 2):
                print(floor)
                break
