def DFS(graph, cur, value):
    global max_node, max_value, visit
    if visit[cur]:
        return

    if value > max_value:
        max_node = cur
        max_value = value

    visit[cur] = True
    for node in graph[cur]:
        DFS(graph, node[0], value + node[1])


v = int(input())
graph = [[] for _ in range(v + 1)]
visit = [False for _ in range(v+1)]
for i in range(v):
    temp = list(map(int, input().split()))
    start = temp[0]
    node = temp[1:-1]
    for j in range(0, len(node), 2):
        graph[start].append([node[j], node[j + 1]])
max_node = 1
max_value = 0
DFS(graph, 1, 0)
visit = [False for i in range(v+1)]
temp = max_node
max_node = 1
max_value = 0
DFS(graph, temp, 0)
print(max_value)
