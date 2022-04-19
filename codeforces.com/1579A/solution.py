for i in range(int(input())):
    s = input()

    if len(s) % 2 == 1:
        print('NO')
    else:
        letter_counts = {'A': 0, 'B': 0, 'C': 0}
        for c in s:
            letter_counts[c] += 1
        if letter_counts['B'] == letter_counts['A'] + letter_counts['C']:
            print('YES')
        else:
            print('NO')
