for i in range(int(input())):
    number_of_stones = int(input())
    stone_powers = list(map(int, input().split()))

    min_elem_coordinate = 0
    max_elem_coordinate = 0
    min_elem = stone_powers[0]
    max_elem = stone_powers[0]

    for j in range(number_of_stones):
        if stone_powers[j] < min_elem:
            min_elem = stone_powers[j]
            min_elem_coordinate = j
        elif stone_powers[j] > max_elem:
            max_elem = stone_powers[j]
            max_elem_coordinate = j

    min_coord = min(min_elem_coordinate, max_elem_coordinate)
    max_coord = max(min_elem_coordinate, max_elem_coordinate)

    print(min(
        max_coord + 1,  # from the left
        number_of_stones - min_coord,  # from the right,
        min_coord + 1 + number_of_stones - max_coord  # left and right
    ))
