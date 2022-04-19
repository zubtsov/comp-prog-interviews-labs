for i in range(int(input())):
    str = input()
    str_len = len(str)

    if str_len % 2 == 1:
        print('NO')
    else:
        for i in range(str_len // 2):
            if str[i] != str[i + str_len // 2]:
                print('NO')
                break
        else:
            print('YES')
