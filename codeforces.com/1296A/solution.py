for i in range(int(input())):
    num_of_elements = int(input())
    elements = list(map(int, input().split()))

    odd_elems = 0
    even_elems = 0
    sum_of_elems = 0

    for j in range(num_of_elements):
        if elements[j] & 1 == 0:
            even_elems += 1
        else:
            odd_elems += 1
        sum_of_elems += elements[j]

    if sum_of_elems & 1 != 0 or (even_elems > 0 and odd_elems > 0):
        print('YES')
    else:
        print('NO')
