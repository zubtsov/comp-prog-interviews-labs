number_of_football_teams = int(input())

home_uniforms_colors = [None] * number_of_football_teams
guest_uniforms_colors = [None] * number_of_football_teams

team_plays_in_guest_form_games_number = 0

for team_number in range(number_of_football_teams):
    home_uniform_color, guest_uniform_color = map(int, input().split())
    for other_team_number in range(team_number):
        if home_uniforms_colors[other_team_number] == guest_uniform_color:
            team_plays_in_guest_form_games_number += 1
        if guest_uniforms_colors[other_team_number] == home_uniform_color:
            team_plays_in_guest_form_games_number += 1

    home_uniforms_colors[team_number] = home_uniform_color
    guest_uniforms_colors[team_number] = guest_uniform_color

print(team_plays_in_guest_form_games_number)
