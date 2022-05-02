for t in range(int(input())):
    source_s = input()
    target_s = input()

    for i in range(len(source_s)):
        if i % 2 == 0 and (len(source_s) - i - 1) % 2 == 0 and target_s == source_s[i]:
            print('YES')
            break
    else:
        print('NO')
