import sys

N, M = map(int, sys.stdin.readline().strip().split())
move = [-1 for i in range(101)]
for i in range(N + M):
    x, y = map(int, sys.stdin.readline().strip().split())
    move[x] = y

que = [[1,0]]
visited = [-1 for i in range(101)]
answer = 1000000
while que:
    pop = que.pop(0)
    position = pop[0]
    cnt = pop[1]
    for i in range(position, position + 7):
        if i <= 100 and visited[i] == -1:
            if i <= 100 and move[i] != -1:
                que.append([move[i], cnt + 1])
                visited[move[i]] = cnt + 1
                visited[i] = cnt + 1
            else:
                que.append([i, cnt + 1])
                visited[i] = cnt + 1

print(visited[100])
