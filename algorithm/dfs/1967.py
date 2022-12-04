import sys
sys.setrecursionlimit(10**5)

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
visit = [False for _ in range(v + 1)]
for i in range(v - 1):
    s, e, d = map(int, input().split())
    graph[s].append([e, d])
    graph[e].append([s, d])
max_node = 1
max_value = 0
DFS(graph, 1, 0)
visit = [False for i in range(v + 1)]
temp = max_node
max_node = 1
max_value = 0
DFS(graph, temp, 0)
print(max_value)
