dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
N = int(input())
arr = [[0 for j in range(N)] for i in range(N)]
heartX = 0
heartY = 0
for i in range(N):
    tmp = input()
    for j in range(N):
        arr[i][j] = tmp[j]

for i in range(N):
    for j in range(N):
        if arr[i][j] == '*' and 0 < i < N - 1 and 0 < j < N - 1:
            cnt = 0
            for k in range(4):
                if arr[i + dy[k]][j + dx[k]] == '*':
                    cnt += 1
            if cnt == 4:
                heartY = i
                heartX = j

answer = [0, 0, 0, 0, 0]
for i in range(1, N):
    if 0 <= heartX - i < N and arr[heartY][heartX - i] == '*':
        answer[0] += 1
    if 0 <= heartX + i < N and arr[heartY][heartX + i] == "*":
        answer[1] += 1
    if 0 <= heartY + i < N and arr[heartY + i][heartX] == '*':
        answer[2] += 1
    if 0 <= heartY + i < N and arr[heartY + i][heartX - 1] == '*':
        answer[3] += 1
    if 0 <= heartY + i < N and arr[heartY + i][heartX + 1] == '*':
        answer[4] += 1
print(str(heartY+1) + " " + str(heartX+1))
for i in answer:
    print(i, end=" ")
