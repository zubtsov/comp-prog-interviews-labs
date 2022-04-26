for i in range(int(input())):
    array_length = int(input())
    array = map(int, input().split())

    s = sum(array)

    if s < array_length:
        print(1)
    else:
        print(s - array_length)
