import sys

N = sys.stdin.readline().strip()
num = ' '
for i in range(1, 100001):
    num += str(i) + " "
idx = -1
for ch in N:
    for j in range(idx + 1, len(num)):
        if ch == num[j]:
            idx = j
            break
start, end = idx, idx
while num[start] != ' ':
    start -= 1
while num[end] != ' ':
    end += 1
ans = int(num[start+1: end])
print(ans)
