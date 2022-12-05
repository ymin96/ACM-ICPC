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
                heapq.heappush(que, [cost, next[0]])


INF = 9999999999999
n, m, x = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)
answer = [0 for i in range(n + 1)]
for i in range(m):
    s, e, d = map(int, input().split())
    graph[s].append([e, d])
for i in range(1, n + 1):
    distance = [INF] * (n + 1)
    dijkstra(i)
    if i != x:
        answer[i] += distance[x]
    else:
        for j in range(1, n + 1):
            answer[j] += distance[j]
print(max(answer))
