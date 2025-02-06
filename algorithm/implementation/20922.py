import sys

N, K = map(int, sys.stdin.readline().strip().split())

lst = list(map(int, sys.stdin.readline().strip().split()))

visit = [0 for i in range(100001)]

front = 0
rear = 1
answer = 1
cnt = 1
visit[lst[0]] = 1
while rear < len(lst):
    if visit[lst[rear]] < K:
        visit[lst[rear]] += 1
        rear += 1
        cnt += 1
    else:
        visit[lst[front]] -= 1
        cnt -= 1
        front += 1
    answer = max(answer, cnt)
print(answer)
