number_of_invited_friends = int(input())

gift_receptions = [0] * number_of_invited_friends

gift_receiver_id = 1

for gift_giver_id in map(int, input().split()):
    gift_receptions[gift_giver_id - 1] = str(gift_receiver_id)
    gift_receiver_id += 1

print(' '.join(gift_receptions))
