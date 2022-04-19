for i in range(int(input())): # TODO: prove and improve the solution
    xyz = list(map(int, input().split()))
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]

    vars = [[xyz[i], xyz[j], xyz[k]] for i in range(3) for j in range(3) for k in range(3)]

    for v in vars:
        xt = max(v[0], v[1])
        yt = max(v[0], v[2])
        zt = max(v[1], v[2])

        if xt == x and yt == y and zt == z:
            print('YES')
            print(' '.join(map(str, v)))
            break
    else:
        print('NO')
