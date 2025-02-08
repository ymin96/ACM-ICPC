import sys

N, D = map(int, sys.stdin.readline().strip().split())
lst = []
for i in range(N):
    lst.append(list(map(int, sys.stdin.readline().strip().split())))
dp = [i for i in range(D + 1)]

lst.sort(key=lambda x: (x[0], x[1], x[2]))

for i in lst:
    start = i[0]
    end = i[1]
    distance = i[2]
    for j in range(end, D + 1):
        dp[j] = min(dp[j], dp[start] + distance + (j - end))

print(dp[-1])
