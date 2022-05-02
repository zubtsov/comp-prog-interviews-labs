for t in range(int(input())):
    array_len = int(input())
    array = list(map(int, input().split()))

    min_elem = array[0]
    num_of_min_elems = 1

    for i in range(1, array_len):
        if array[i] < min_elem:
            min_elem = array[i]
            num_of_min_elems = 1
        elif array[i] == min_elem:
            num_of_min_elems += 1

    print(array_len - num_of_min_elems)
