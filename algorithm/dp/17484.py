import sys

INF = 999999999999
N, M = map(int, sys.stdin.readline().split())
lst = []
dp = [[[INF for j in range(M + 2)] for i in range(N)] for k in range(3)]
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().split())))
    lst[i].append(INF)
    lst[i].insert(0, INF)

for k in range(3):
    for i in range(1, M + 1):
        dp[k][0][i] = lst[0][i]

for i in range(1, N):
    for j in range(1, M + 1):
        for k in range(3):
            if k == 0:
                dp[k][i][j] = lst[i][j] + min(dp[1][i - 1][j], dp[2][i - 1][j + 1])
            elif k == 1:
                dp[k][i][j] = lst[i][j] + min(dp[0][i - 1][j - 1], dp[2][i - 1][j + 1])
            elif k == 2:
                dp[k][i][j] = lst[i][j] + min(dp[0][i - 1][j - 1], dp[1][i - 1][j])
ans = INF
for i in range(3):
    ans = min(ans, min(dp[i][-1]))
print(ans)
