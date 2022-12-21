from sys import stdin

n, m = map(int, input().split())
lst = []
for i in range(n):
    lst.append(list(map(int, stdin.readline().split())))
    for j in range(1, n):
        lst[i][j] += lst[i][j - 1]
    if i > 0:
        for j in range(n):
            lst[i][j] += lst[i - 1][j]
for _ in range(m):
    y1, x1, y2, x2 = map(int, stdin.readline().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    answer = lst[y2][x2]
    if x1 > 0:
        answer -= lst[y2][x1 - 1]
    if y1 > 0:
        answer -= lst[y1 - 1][x2]
    if x1 > 0 and y1 > 0:
        answer += lst[y1 - 1][x1 - 1]
    print(answer)
