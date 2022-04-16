from math import ceil

for i in range(int(input())):
    park_height, park_width = map(int, input().split())
    print(ceil(park_width * park_height / 2))
