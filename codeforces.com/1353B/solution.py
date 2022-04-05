number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    number_of_elements, maximum_number_of_moves = map(int, input().split())

    a_array = list(map(int, input().split()))
    b_array = list(map(int, input().split()))

    a_array.sort()
    b_array.sort()

    sum_of_elems = 0
    for j in range(number_of_elements):
        b_next = b_array[number_of_elements - j - 1]
        a_next = a_array[j]

        if j < maximum_number_of_moves:
            sum_of_elems += max(b_next, a_next)
        else:
            sum_of_elems += a_next

    print(sum_of_elems)
