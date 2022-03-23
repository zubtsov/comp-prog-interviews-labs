number_of_stones = input()
stones = input()

number_of_removals = 0

for i in range(1, len(stones)):
    if stones[i-1] == stones[i]:
        number_of_removals += 1

print(number_of_removals)
