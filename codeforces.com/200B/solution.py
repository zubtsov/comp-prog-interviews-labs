number_of_drinks = int(input())

percentages = list(map(int, input().split()))

print(sum(percentages) / len(percentages))
