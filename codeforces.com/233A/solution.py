permutation_size = int(input())

if permutation_size % 2 == 1:
    print(-1)
else:
    print(' '.join([str(i+1) + ' ' + str(i) for i in range(1, permutation_size, 2)]))
