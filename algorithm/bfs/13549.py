from collections import deque

n, k = map(int, input().split())

INF = 99999999999
visit = [INF] * 100001
que = deque()
que.append([n, 0])
visit[n] = 0
while que:
    x, dist = que.popleft()
    if visit[k] != INF:
        break
    if 0 <= x - 1 <= 100000 and dist + 1 < visit[x - 1]:
        visit[x - 1] = dist + 1
        que.append([x - 1, dist + 1])
    if 0 <= x + 1 <= 100000 and dist + 1 < visit[x + 1]:
        visit[x + 1] = dist + 1
        que.append([x + 1, dist + 1])
    if 0 <= x * 2 <= 100000 and dist < visit[x * 2]:
        visit[x * 2] = dist
        que.appendleft([x * 2, dist])
print(visit[k])
