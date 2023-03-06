cards = input().split()

first_team_players = []
second_team_players = []
terminator = False

for card in cards:
    if card in first_team_players or card in second_team_players:
        continue
    card_args = card.split('-')
    team_name = card_args[0]
    player_number = card_args[1]
    is_first_team = team_name == 'A'

    if is_first_team:
        first_team_players.append(card)
    else:
        second_team_players.append(card)

    if len(first_team_players) > 4 or len(second_team_players) > 4:
        terminator = True
        break

print(f'Team A - {11-len(first_team_players)}; Team B - {11-len(second_team_players)}')
if terminator:
    print('Game was terminated')