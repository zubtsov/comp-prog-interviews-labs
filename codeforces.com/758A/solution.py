max_theoretical_welfare = 1000000

number_of_citizens = int(input())

total_money_spent = 0
max_welfare = 0

for current_welfare in map(int, input().split()):
    total_money_spent += (max_theoretical_welfare - current_welfare)
    if current_welfare > max_welfare:
        max_welfare = current_welfare

print(total_money_spent - number_of_citizens * (max_theoretical_welfare - max_welfare))
