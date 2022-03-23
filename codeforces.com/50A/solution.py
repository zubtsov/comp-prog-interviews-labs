board_width, board_length = list(map(int, input().split()))
domino_length = 2

if board_width % 2 == 0:
    print((board_width // domino_length) * board_length)
elif board_length % 2 == 0:
    print((board_length // domino_length) * board_width)
else:
    print((board_width * board_length) // domino_length)
