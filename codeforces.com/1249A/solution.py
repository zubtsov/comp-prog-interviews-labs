for q in range(int(input())):
    number_of_students = int(input())
    students_skills = list(map(int, input().split()))
    students_skills.sort()

    number_of_teams = 1
    for i in range(1, number_of_students):
        if abs(students_skills[i-1] - students_skills[i]) == 1:
            number_of_teams += 1
            break

    print(number_of_teams)
