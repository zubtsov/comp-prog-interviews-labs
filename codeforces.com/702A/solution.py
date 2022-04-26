array_length = int(input())
array = list(map(int, input().split()))

seq_start = 0
seq_end = 0
max_inc_seq_len = 0

if array_length == 1:
    print(1)
else:
    for i in range(1, array_length):
        if array[i - 1] < array[i]:
            seq_end = i
        else:
            if seq_end - seq_start + 1 > max_inc_seq_len:
                max_inc_seq_len = seq_end - seq_start + 1
            seq_start = seq_end = i
    else:  # TODO: check if it's possible to refactor
        if seq_end - seq_start + 1 > max_inc_seq_len:
            max_inc_seq_len = seq_end - seq_start + 1

    print(max_inc_seq_len)
