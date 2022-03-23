number_of_participants, participant_with_threshold_score = map(int, input().split(' '))
participants_scores = list(map(int, input().split(' ')))

threshold_score = participants_scores[participant_with_threshold_score - 1]

for i in range(number_of_participants + 1):
    if i == number_of_participants or participants_scores[i] < threshold_score or participants_scores[i] <= 0:
        print(i)
        break
