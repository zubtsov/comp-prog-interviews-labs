for i in range(int(input())):
    seq_len = int(input())
    seq = input().split()

    restored_seq = [seq[i] + ' ' + seq[-i-1] for i in range(seq_len // 2)]

    if seq_len % 2 == 1:
        restored_seq.append(seq[seq_len // 2])

    print(' '.join(restored_seq))
