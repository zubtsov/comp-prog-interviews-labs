first_banana_cost,initial_dollar_amount,target_bananas_number = map(int, input().split())

borrowed_dollar_amount = first_banana_cost * (1 + target_bananas_number) * target_bananas_number / 2 - initial_dollar_amount

if borrowed_dollar_amount < 0:
    print(0)
else:
    print(int(borrowed_dollar_amount))
