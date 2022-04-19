n, m = map(int, input().split())
# TODO: refactor
for i in range(n+1, m + 1):
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            break  # not prime
    else:
        if i == m:
            print('YES')
        else:
            print('NO')
        break
else:
    if i == m:
        print('NO')
    else:
        print('YES')
