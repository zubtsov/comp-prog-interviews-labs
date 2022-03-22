number_of_problems = int(input())
number_of_solutions = 0

for i in range(number_of_problems):
    degree_of_confidence = sum(map(int, input().split(' ')))
    if degree_of_confidence > 1:
        number_of_solutions += 1

print(number_of_solutions)
