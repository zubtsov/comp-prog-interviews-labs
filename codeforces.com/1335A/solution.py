number_of_cases = int(input())

for i in range(number_of_cases):
    number_of_candies = int(input())
    print(number_of_candies // 2 - (1 - number_of_candies % 2))
