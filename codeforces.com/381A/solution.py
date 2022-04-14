number_of_cards = int(input())

cards_values = list(map(int, input().split()))

i = 0
j = number_of_cards - 1
k = 0

scores = [0, 0]

while i <= j:
    if cards_values[i] > cards_values[j]:
        scores[k % 2] += cards_values[i]
        i += 1
        k += 1
    else:
        scores[k % 2] += cards_values[j]
        j -= 1
        k += 1

print(' '.join(map(str, scores)))
