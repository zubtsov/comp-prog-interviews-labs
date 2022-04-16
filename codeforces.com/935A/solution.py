number_of_employees = int(input())

possible_divisions = 1
# TODO: how to prove that it can only be solved with a brute force?
for i in range(2, number_of_employees // 2 + 1):
    if (number_of_employees - i) % i == 0:
        possible_divisions += 1

print(possible_divisions)
