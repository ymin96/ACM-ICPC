from sys import stdin
from collections import deque

global tree, answer
n = int(stdin.readline())
tree = [[] for i in range(n + 1)]
answer = [0 for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
que = deque([1])
answer[1] = 1

while que:
    pop = que.popleft()
    for i in tree[pop]:
        if answer[i] != 0:
            continue
        que.append(i)
        answer[i] = pop

for i in range(2, n+1):
    print(answer[i])
