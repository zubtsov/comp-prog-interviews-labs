from math import sqrt, floor

number_of_problems, party_route_time_minutes = map(int, input().split())

time_for_contest_minutes = 4 * 60 - party_route_time_minutes

max_problems_number = floor((-1 + sqrt(1 + 8 * time_for_contest_minutes / 5)) / 2)
print(min(number_of_problems, max_problems_number))  # solved quadratic equation
