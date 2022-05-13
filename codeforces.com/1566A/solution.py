from math import ceil

for t in range(int(input())):
    length_of_array, sum_of_elements = map(int, input().split())

    index_of_median = ceil(length_of_array / 2) - 1
    number_of_zeros = index_of_median
    median_value = int(sum_of_elements / (length_of_array - number_of_zeros))

    print(median_value)
