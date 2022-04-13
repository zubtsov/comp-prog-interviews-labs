number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    array_length = int(input())
    array = list(map(int, input().split()))

    min_elem = array[0]
    max_elem = array[0]

    for e in array:
        min_elem = min(min_elem, e)
        max_elem = max(max_elem, e)

    print(max_elem - min_elem)
