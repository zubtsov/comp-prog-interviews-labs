for i in range(int(input())):
    skills = list(map(int, input().split()))

    if max(skills[:2]) > min(skills[2:]) and max(skills[2:]) > min(skills[:2]):
        print('YES')
    else:
        print('NO')
