import sys

H, W = map(int, sys.stdin.readline().strip().split())
info = list(map(int, sys.stdin.readline().strip().split()))

field = [[0 for j in range(W)] for i in range(H)]
answer = 0

for i in range(W):
    for j in range(info[i]):
        field[j][i] = 1

for i in range(H):
    for j in range(W):
        if field[i][j] == 0:
            left = False
            right = False
            for k in range(j - 1, -1, -1):
                if field[i][k] == 1:
                    left = True
                    break
            for k in range(j, W):
                if field[i][k] == 1:
                    right = True
                    break
            if right and left:
                answer += 1

print(answer)
