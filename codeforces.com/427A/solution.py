number_of_events = int(input())

current_capacity = 0
crimes_committed = 0

for n in map(int, input().split()):
    if n == -1 and current_capacity == 0:
        crimes_committed += 1
    else:
        current_capacity += n

print(crimes_committed)
