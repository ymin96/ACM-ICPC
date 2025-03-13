import sys

N = int(sys.stdin.readline().strip())

lst = list(map(int, sys.stdin.readline().strip().split()))

lst.sort()

ansl = 0
ansr = len(lst) - 1
ans = abs(lst[0] + lst[-1])

left = 0
right = len(lst) - 1

while left < right:
    temp = lst[left] + lst[right]
    if abs(temp) < ans:
        ansl = left
        ansr = right
        ans = abs(temp)

    if temp > 0:
        right -= 1
    else:
        left += 1

print(str(lst[ansl]) + " " + str(lst[ansr]))
