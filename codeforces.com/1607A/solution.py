for i in range(int(input())):
    keyboard_positions = dict([(v, k) for k, v in enumerate(input())])
    word_to_type = input()

    moves = 0
    last_pos = keyboard_positions[word_to_type[0]]

    for c in word_to_type:
        current_pos = keyboard_positions[c]
        moves += abs(last_pos - current_pos)
        last_pos = current_pos

    print(moves)