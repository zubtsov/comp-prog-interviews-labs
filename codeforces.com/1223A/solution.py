for t in range(int(input())):
    number_of_matches = int(input())

    if number_of_matches < 4:
        print(4 - number_of_matches)
    elif number_of_matches % 2 == 0:
        print(0)
    else:
        print(1)
