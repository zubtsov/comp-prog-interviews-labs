number_of_test_cases = int(input())

known_numbers = [1]

for i in range(number_of_test_cases):
    k = int(input())

    for l in range(len(known_numbers), k):
        j = known_numbers[-1] + 1
        while j % 3 == 0 or j % 10 == 3:
            j += 1
        known_numbers.append(j)

    print(known_numbers[k - 1])
