for i in range(int(input())):
    arr_len = int(input())
    elems = list(map(int, input().split()))

    odd_elements_parity = elems[0] % 2
    even_elements_parity = elems[1] % 2

    for j in range(arr_len):
        if j % 2 == 0:  # odd elems
            if elems[j] % 2 != odd_elements_parity:
                print('NO')
                break
        else:  # even elems
            if elems[j] % 2 != even_elements_parity:
                print('NO')
                break
    else:
        print('YES')
