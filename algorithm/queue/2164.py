import sys
from collections import deque
N = int(sys.stdin.readline())
queue = deque(list(i for i in range(1, N + 1)))
while len(queue) > 1:
    queue.popleft()
    temp = queue.popleft()
    queue.append(temp)
print(queue.pop())
