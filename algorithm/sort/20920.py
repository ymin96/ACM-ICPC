import sys

N, M = map(int, sys.stdin.readline().split())
dic = dict()
for i in range(N):
    word = sys.stdin.readline().strip()
    if len(word) >= M:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
lst = [[k, v] for k, v in dic.items()]
lst.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))
for ans in lst:
    print(ans[0])
