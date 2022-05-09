for t in range(int(input())):
    arr_len = int(input())
    arr = list(map(int, input().split()))

    max_left = [arr[0]]
    min_right = [arr[arr_len - 1]]

    for i in range(1, arr_len - 1):
        max_left.append(max(max_left[i-1], arr[i]))
        min_right.append(min(min_right[i-1], arr[arr_len - i - 1]))

    for i in range(0, arr_len - 1):
        if max_left[i] > min_right[arr_len - i - 2]:
            print('YES')
            break
    else:
        print('NO')
