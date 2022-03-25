number_of_stops = int(input())

max_capacity = 0
current_number_of_passengers = 0

for i in range(number_of_stops):
    out_passengers_number, in_passengers_number = map(int, input().split())
    current_number_of_passengers = current_number_of_passengers - out_passengers_number + in_passengers_number
    if current_number_of_passengers > max_capacity:
        max_capacity = current_number_of_passengers

print(max_capacity)
