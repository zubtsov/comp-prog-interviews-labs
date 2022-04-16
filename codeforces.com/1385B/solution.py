for i in range(int(input())):
    permutation_length = int(input())
    merged_permutation = input().split()
    permutation = dict.fromkeys(merged_permutation)
    print(' '.join(permutation.keys()))
