dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    lst = []
    visit = [[0 for x in range(m)] for y in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        visit[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if visit[i][j] == 1:
                cnt += 1
                que = []
                que.append([i, j])
                visit[i][j] = 0
                while que:
                    pop = que.pop()
                    y = pop[0]
                    x = pop[1]
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if -1 >= ny or ny >= n or -1 >= nx or nx >= m or visit[ny][nx] == 0:
                            continue
                        que.append([ny, nx])
                        visit[ny][nx] = 0
    print(cnt)
