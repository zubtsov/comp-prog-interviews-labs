import re

for i in range(int(input())):
    picture_length = int(input())
    picture_to_make = input()

    stamp_sequences = re.split(r'W+', picture_to_make)

    for seq in stamp_sequences:
        if len(seq) == 0:
            continue
        elif len(set(seq)) == 1:
            print('NO')
            break
    else:
        print('YES')
