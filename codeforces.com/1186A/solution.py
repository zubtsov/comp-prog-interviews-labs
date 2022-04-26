number_of_participants, number_of_pens, number_of_notebooks = map(int, input().split())

if number_of_pens >= number_of_participants and number_of_notebooks >= number_of_participants:
    print('Yes')
else:
    print('No')
