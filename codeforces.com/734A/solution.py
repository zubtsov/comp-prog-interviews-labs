input()

games_result = sum(map(lambda n: 1 if n == 'A' else -1, input()))

if games_result > 0:
    print('Anton')
elif games_result == 0:
    print('Friendship')
else:
    print('Danik')
