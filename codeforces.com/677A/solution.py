number_of_friends, height_of_fence = map(int, input().split())

required_road_width = 0

for friend_height in map(int, input().split()):
    if friend_height > height_of_fence:
        required_road_width += 2
    else:
        required_road_width += 1

print(required_road_width)
