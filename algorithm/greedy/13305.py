import sys

N = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))
price[-1] = 0
ans = 0
front = 0
while True:
    temp = 0
    for rear in range(front + 1, len(price)):
        temp += price[front] * distance[rear - 1]
        if price[rear] < price[front]:
            front = rear
            break
    ans += temp
    if front >= len(price) - 1:
        break
print(ans)
