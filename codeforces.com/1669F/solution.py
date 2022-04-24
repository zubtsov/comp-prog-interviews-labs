for i in range(int(input())):
    number_of_candies = int(input())
    candies_weights = list(map(int, input().split()))

    bob_pos = number_of_candies - 1
    alice_pos = 0

    bob_current_weight = 0
    alice_current_weight = 0

    last_equal_candies_total_number = 0

    while alice_pos <= bob_pos:
        if alice_current_weight <= bob_current_weight:
            alice_current_weight += candies_weights[alice_pos]
            alice_pos += 1
        else:
            bob_current_weight += candies_weights[bob_pos]
            bob_pos -= 1

        if alice_current_weight == bob_current_weight:
            last_equal_candies_total_number = alice_pos + (number_of_candies - bob_pos - 1)

    print(last_equal_candies_total_number)
