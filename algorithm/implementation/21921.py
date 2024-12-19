import sys

N, X = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
tmp = sum(lst[0:X])
sumList = [tmp]
for i in range(X, len(lst)):
    tmp += lst[i]
    tmp -= lst[i - X]
    sumList.append(tmp)
sumList.sort()
if sumList[-1] == 0:
    print("SAD")
else:
    print(sumList[-1])
    print(sumList.count(sumList[-1]))

