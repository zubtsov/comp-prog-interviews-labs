for i in range(int(input())):
    set_size = int(input())
    numbers = map(int, input().split())

    odd_numbers = 0
    even_numbers = 0

    for n in numbers:
        if n % 2 == 0:
            even_numbers += 1
        else:
            odd_numbers += 1

    if odd_numbers == even_numbers:
        print('Yes')
    else:
        print('No')
