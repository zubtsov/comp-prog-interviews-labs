from math import sqrt, ceil

number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    width, height = map(int, input().split())

    min_square_side1 = ceil(sqrt(2 * width * height))

    min_square_side2 = min(
        max(2 * width, height),
        max(2 * height, width),
        max(width + height, max(width, height) - min(width, height))
    )

    min_square_area = max(min_square_side1, min_square_side2) ** 2

    print(min_square_area)
