import sys, heapq

N, M = map(int, sys.stdin.readline().strip().split())
INF = 1e8
graph = [[] for i in range(N + 1)]
distance = [INF for i in range(N + 1)]

for i in range(M):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

que = []
heapq.heappush(que, [0, 1])
distance[1] = 0

while que:
    dist, now = heapq.heappop(que)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        if dist + i[1] < distance[i[0]]:
            distance[i[0]] = dist + i[1]
            heapq.heappush(que, [dist + i[1], i[0]])

print(distance[N])
