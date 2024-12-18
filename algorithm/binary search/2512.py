import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline())
lst.sort()

low = 1
high = lst[-1]
ans = 1

while low <= high:
    mid = int(low + (high - low) / 2)
    temp = 0
    for i in lst:
        if i > mid:
            temp += mid
        else:
            temp += i
    if temp > M:
        high = mid - 1
    else:
        ans = mid
        low = mid + 1
print(ans)
