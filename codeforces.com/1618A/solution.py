for t in range(int(input())):
    b_numbers = list(map(int, input().split()))

    a_numbers = b_numbers[:2]

    if b_numbers[2] != sum(a_numbers):
        a_numbers += [b_numbers[2]]
    else:
        a_numbers += [b_numbers[3]]

    print(' '.join(map(str, a_numbers)))
