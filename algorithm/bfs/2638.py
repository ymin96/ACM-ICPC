dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
array = []
end = 0
for i in range(n):
    array.append(list(map(int, input().split())))
    end += array[i].count(1)
answer = 0
while end > 0:
    visit = [[False for x in range(m)] for y in range(n)]
    que = [[0, 0]]
    visit[0][0] = True
    while que:
        y, x = que.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if -1 >= ny or ny >= n or -1 >= nx or nx >= m:
                continue
            if array[ny][nx] == 0 and not visit[ny][nx]:
                que.append([ny, nx])
                visit[ny][nx] = True
    delete = []
    for i in range(n):
        for j in range(m):
            if array[i][j] == 1:
                cnt = 0
                for k in range(4):
                    ny = i + dy[k]
                    nx = j + dx[k]
                    if visit[ny][nx]:
                        cnt += 1
                if cnt >= 2:
                    delete.append([i, j])
    end -= len(delete)
    for y, x in delete:
        array[y][x] = 0
    answer += 1
print(answer)
