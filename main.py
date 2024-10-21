team = {
    'player_1': '#1',
    'player_2': '#32',
    'player_3': '#5',
    'player_4': '#7',
    'player_5': '#99',
    'player_6': '#17',
    'player_7': '#8'
}
team_2 = {
    'player_1': '#1',
    'player_2': '#32'
}
team_3 = {
    'player_1': '#1'
}


def on_court(team):
    if len(team) > 5:
        while True:
            team_on_court = []
            for number in team.values():
                if len(team_on_court) <= 4:
                    team_on_court.append(number)
            print(f'максимальное количество игроков {team_on_court} на площадке')
            break
    elif len(team) < 2:
        print(f'команда не может продолжать игру')
    else:
        team_on_court = []
        for number in team.values():
            team_on_court.append(number)
        print(f'минимальное количество игроков {team_on_court} на площадке')


on_court(team)
on_court(team_2)
on_court(team_3)
