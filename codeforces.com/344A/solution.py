number_of_magnets = int(input())

last_polarity = input()
number_of_groups = 1

for i in range(number_of_magnets - 1):
    polarity = input()
    if polarity != last_polarity:
        number_of_groups += 1
        last_polarity = polarity

print(number_of_groups)
