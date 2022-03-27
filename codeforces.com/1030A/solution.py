number_of_opinions = int(input())

complexity = 'EASY'

for opinion in input().split():
    if opinion == '1':
        complexity = 'HARD'
        break

print(complexity)

