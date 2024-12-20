import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n, k, teamID, m = map(int, sys.stdin.readline().strip().split())
    teamRank = [[0 for j in range(3)] for i in range(n)]
    teamScore = [[0 for j in range(k)] for i in range(n)]
    for z in range(m):
        i, j, s = map(int, sys.stdin.readline().strip().split())
        i -= 1
        j -= 1
        teamScore[i][j] = max(teamScore[i][j], s)
        teamRank[i][1] += 1
        teamRank[i][2] = z
    for i in range(n):
        teamRank[i][0] = sum(teamScore[i])
        teamRank[i].append(i + 1)
    teamRank.sort(key=lambda x: (-x[0], x[1], x[2]))
    for i in range(len(teamRank)):
        if teamRank[i][3] == teamID:
            print(i + 1)
            break
