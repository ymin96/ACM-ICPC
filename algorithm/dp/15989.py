import sys

N = int(sys.stdin.readline().strip())

dp = [[0 for j in range(4)] for i in range(10001)]

dp[1][1] = 1
dp[2][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, 10001):
    dp[i][1] = dp[i-1][1]
    dp[i][2] = dp[i-2][1] + dp[i-2][2]
    dp[i][3] = dp[i-3][1] + dp[i-3][2] + dp[i-3][3]


for i in range(N):
    a = int(sys.stdin.readline().strip())
    print(sum(dp[a]))