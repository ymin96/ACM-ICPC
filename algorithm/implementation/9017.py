T = int(input())
for k in range(T):
    N = int(input())
    record_list = list(map(int, input().split()))
    team = dict()
    team_total = dict()
    for record in record_list:
        if record not in team:
            team[record] = 1
        else:
            team[record] += 1
    for key in team.keys():
        if team[key] >= 6:
            team_total[key] = [key, 0, 0, 0]
    cnt = 1
    score = 1
    for record in record_list:
        if record in team_total:
            if team_total[record][1] <= 4:
                if team_total[record][1] < 4:
                    team_total[record][1] += 1
                    team_total[record][2] += score
                elif team_total[record][1] == 4:
                    team_total[record][1] += 1
                    team_total[record][3] = cnt
                    cnt += 1
            score += 1
    team_list = list(team_total.values())
    team_list.sort(key=lambda x: (x[2], x[3]))
    print(team_list[0][0])
