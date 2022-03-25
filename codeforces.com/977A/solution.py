minuend, number_of_subtractions = map(int, input().split())

for i in range(number_of_subtractions):
    if minuend % 10 == 0:
        minuend /= 10
    else:
        minuend -= 1

print(int(minuend))
