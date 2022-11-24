def find(parent, x):
    if x == parent[x]:
        return x
    else:
        y = find(parent,parent[x])
        parent[x] = y
        return y


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)

    if x == y:
        return

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())
truth = list(map(int, input().split()))[1:]
room = [_ for _ in range(m + 1)]
people = [[] for _ in range(n + 1)]
for i in range(m):
    temp = list(map(int, input().split()))[1:]
    for j in temp:
        people[j].append(i + 1)
for i in range(1, len(people)):
    for j in range(len(people[i]) - 1):
        union(room, people[i][j], people[i][j + 1])
lst = []
for i in truth:
    lst.append(find(room, i))
ans = 0
for i in range(1, len(room)):
    if lst.count(room[i]) == 0:
        ans += 1
print(ans)
