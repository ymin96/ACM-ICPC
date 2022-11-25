


v = int(input())
graph = [[] for _ in range(v + 1)]
value = [[0 for j in range(v + 1)] for i in range(v + 1)]
for i in range(v):
    temp = list(map(int, input().split()))
    start = temp[0]
    node = temp[1:-1]
    for j in range(0, len(node), 2):
        graph[start].append(node[j])
        value[start][node[j]] = node[j + 1]
print(graph)
