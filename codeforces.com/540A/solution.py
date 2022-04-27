def min_moves(original, target):
    return min((original - target) % 10, (target - original) % 10)


number_of_discs = int(input())

original_state = [int(c) for c in input()]

target_state = [int(c) for c in input()]

print(sum([min_moves(o, t) for o, t in zip(original_state, target_state)]))
