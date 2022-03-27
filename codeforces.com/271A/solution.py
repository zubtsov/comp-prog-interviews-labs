year_number = int(input())


# TODO: proof that it can only be solved with the brute force
def has_repeating_digits(year):
    return len(set(year)) < 4


answer = year_number + 1

while has_repeating_digits(str(answer)):
    answer += 1

print(answer)
