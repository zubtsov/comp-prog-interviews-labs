TUNA_SUSHI_TYPE = 1
EEL_SUSHI_TYPE = 2

pieces_of_sushi = int(input())
types_of_sushi = list(map(int, input().split()))

last_tuna_count = 0
last_eel_count = 0
last_sushi_type = types_of_sushi[0]
max_length = 0

for i in range(pieces_of_sushi):
    if types_of_sushi[i] == last_sushi_type:
        if types_of_sushi[i] == TUNA_SUSHI_TYPE:
            last_tuna_count += 1
        else:
            last_eel_count += 1
    else:
        if last_sushi_type == TUNA_SUSHI_TYPE:
            last_eel_count = 1
        else:
            last_tuna_count = 1
        last_sushi_type = types_of_sushi[i]

    new_max_length = min(last_tuna_count, last_eel_count) * 2
    if max_length < new_max_length:
        max_length = new_max_length

print(max_length)
