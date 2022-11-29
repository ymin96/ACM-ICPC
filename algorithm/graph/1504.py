import heapq


def dijkstra(start):
    global distance, graph
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0

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
start, end = map(int, input().split())
dijkstra(start)
print(distance[end])
