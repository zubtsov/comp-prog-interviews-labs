number_of_characters = int(input())

if len(set(map(lambda c: c.lower(), input()))) == 26:
    print('YES')
else:
    print('NO')
