number_of_contests = int(input())

scores = list(map(int, input().split()))

number_of_amazing_performances = 0
worst_score = scores[0]
best_score = scores[0]

for score in scores[1:]:
    if score > best_score:
        best_score = score
        number_of_amazing_performances += 1
    elif score < worst_score:
        worst_score = score
        number_of_amazing_performances += 1

print(number_of_amazing_performances)
