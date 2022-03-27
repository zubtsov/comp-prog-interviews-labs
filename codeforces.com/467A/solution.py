number_of_rooms = int(input())

number_of_free_rooms = 0

for i in range(number_of_rooms):
    number_of_tenants, room_capacity = map(int, input().split())
    if room_capacity - number_of_tenants >= 2:
        number_of_free_rooms += 1

print(number_of_free_rooms)
