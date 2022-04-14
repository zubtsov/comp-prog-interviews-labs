number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    burles_to_be_paid = int(input())
    approx_answer = burles_to_be_paid // 3

    if burles_to_be_paid % 3 == 1:
        print(f'{approx_answer + 1} {approx_answer}')
    elif burles_to_be_paid % 3 == 2:
        print(f'{approx_answer} {approx_answer + 1}')
    else:
        print(f'{approx_answer} {approx_answer}')
