import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, sys.stdin.readline().strip().split())

lst = []

for i in range(n):
    lst.append(list(map(int, sys.stdin.readline().strip().split())))

x = 0
y = 0

for i in range(n):
    for j in range(m):
        if lst[i][j] == 2:
            x = j
            y = i

visit = [[-1 for j in range(m)] for i in range(n)]

que = [[x, y, 0]]
visit[y][x] = 0
while que:
    temp = que.pop(0)
    x = temp[0]
    y = temp[1]
    dis = temp[2]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 >= ny or ny >= n or -1 >= nx or nx >= m:
            continue
        if lst[ny][nx] == 1 and visit[ny][nx] == -1:
            que.append([nx, ny, dis + 1])
            visit[ny][nx] = dis + 1

for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            print("0", end=" ")
        else:
            print(visit[i][j], end=" ")
    print("")