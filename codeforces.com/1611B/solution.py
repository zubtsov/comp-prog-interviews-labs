for t in range(int(input())):
    number_of_programmers, number_of_mathematicians = map(int, input().split())

    number_of_teams = min(
        min(number_of_mathematicians, number_of_programmers),
        (number_of_programmers + number_of_mathematicians) / 4
    )

    print(int(number_of_teams))
