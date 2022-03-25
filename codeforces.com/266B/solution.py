queue_size, permutations_simulation_time = map(int, input().split())

queue = list(input())
# TODO: proof, that the minimum computational complexity is O(permutations_simulation_time * queue_size)
for i in range(permutations_simulation_time):
    j = 1
    while j < queue_size:
        if queue[j] == 'G' and queue[j - 1] == 'B':
            queue[j] = 'B'
            queue[j - 1] = 'G'
            j += 2
        else:
            j += 1

print(''.join(queue))
