number_of_soldiers = int(input())

soldiers_heights = list(map(int, input().split()))

max_height = min_height = soldiers_heights[0]
max_height_position = min_height_position = 0

for i in range(1, number_of_soldiers):
    if soldiers_heights[i] > max_height:
        max_height = soldiers_heights[i]
        max_height_position = i
    elif soldiers_heights[i] <= min_height:
        min_height = soldiers_heights[i]
        min_height_position = i

if max_height_position > min_height_position:
    print(max_height_position + (number_of_soldiers - 1) - min_height_position - 1)
else:
    print(max_height_position + (number_of_soldiers - 1) - min_height_position)
