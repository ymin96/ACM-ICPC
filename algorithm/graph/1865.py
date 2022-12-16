def bellman_ford(start, graph, distance):
    global n, m, w, INF
    distance[start] = 0
    edge = len(graph)
    for i in range(n):
        for j in range(edge):
            cur_node, next_node, cost = graph[j]
            if distance[next_node] > distance[cur_node] + cost:
                distance[next_node] = distance[cur_node] + cost
                if i == n - 1:
                    return True
    return False


global n, m, w, INF
INF = int(1e9)
tc = int(input())

for k in range(tc):
    n, m, w = map(int, input().split())
    graph = []
    distance = [INF] * (n + 1)
    for i in range(m):
        s, e, t = map(int, input().split())
        graph.append([s, e, t])
        graph.append([e, s, t])
    for i in range(w):
        s, e, t = map(int, input().split())
        graph.append([s, e, -t])
    cycle = bellman_ford(1, graph, distance)
    if cycle:
        print("YES")
    else:
        print("NO")
