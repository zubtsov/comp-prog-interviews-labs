n = int(input())

number_of_bills = 0

for i in [100, 20, 10, 5]:
    number_of_bills += n // i
    n %= i

print(number_of_bills + n)
