max_personal_participations = 5
team_size = 3

number_of_students, min_team_participations = map(int, input().split())
personal_participations = map(int, input().split())

eligible_personal_participations = len(list(filter(lambda n: n <= max_personal_participations - min_team_participations,
                                                   personal_participations)))

print(int(eligible_personal_participations // team_size))
