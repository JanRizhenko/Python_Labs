results = [
    "Ukraine;2;France;1",
    "Italy;1;Germany;3",
    "France;0;Italy;0",
    "Germany;2;Ukraine;0"
]

table = {}

for line in results:
    team1, score1, team2, score2 = line.split(';')
    score1, score2 = int(score1), int(score2)

    for team in (team1, team2):
        if team not in table:
            table[team] = [0, 0, 0, 0, 0]

    table[team1][0] += 1
    table[team2][0] += 1

    if score1 > score2:
        table[team1][1] += 1
        table[team2][3] += 1
        table[team1][4] += 3
    elif score1 < score2:
        table[team2][1] += 1
        table[team1][3] += 1
        table[team2][4] += 3
    else:
        table[team1][2] += 1
        table[team2][2] += 1
        table[team1][4] += 1
        table[team2][4] += 1

for team, stats in table.items():
    print(f"{team}: {stats[0]} {stats[1]} {stats[2]} {stats[3]} {stats[4]}")
