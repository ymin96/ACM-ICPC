import heapq

def dijkstra(start, distance):
    global graph
    que = []
    heapq.heappush(que, (distance[start], start))

    while que:
        dist, node = heapq.heappop(que)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(que, (cost, next[0]))


n, m = map(int, input().split())
INF = 9999999999999
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)
for i in range(m):
    start, end, dist = map(int, input().split())
    graph[start].append([end, dist])
    graph[end].append([start, dist])
start, end = map(int, input().split())
distance[1] = 0
dijkstra(1, distance)

dist_a1 = [INF] * (n+1)
dist_a1[start] = distance[start]
dijkstra(start, dist_a1)
dist_a2 = [INF] * (n+1)
dist_a2[end] = dist_a1[end]
dijkstra(end, dist_a2)
min_a = dist_a2[-1]

dist_b1 = [INF] * (n+1)
dist_b1[end] = distance[end]
dijkstra(end, dist_b1)
dist_b2 = [INF] * (n+1)
dist_b2[start] = dist_b1[start]
dijkstra(start, dist_b2)
min_b = dist_b2[-1]

if min_a >= INF and min_b >= INF:
    print(-1)
else:
    print(min(min_a, min_b))
