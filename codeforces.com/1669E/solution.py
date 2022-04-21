for t in range(int(input())):
    number_of_strings = int(input())

    pairs = [input() for i in range(number_of_strings)]

    number_of_diff1_pairs = 0

    first_letters = {}
    last_letters = {}
    full_letters = {}

    for i in range(number_of_strings):
        number_of_diff1_pairs += first_letters.get(pairs[i][0], 0) \
                                 + last_letters.get(pairs[i][1], 0) \
                                 - 2 * full_letters.get(pairs[i], 0)

        first_letters[pairs[i][0]] = first_letters.get(pairs[i][0], 0) + 1
        last_letters[pairs[i][1]] = last_letters.get(pairs[i][1], 0) + 1
        full_letters[pairs[i]] = full_letters.get(pairs[i], 0) + 1

    print(number_of_diff1_pairs)
