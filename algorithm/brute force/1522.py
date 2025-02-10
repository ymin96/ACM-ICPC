import sys

lst = sys.stdin.readline().strip()
a = lst.count('a')
lst += lst
answer = 1000000
for i in range(int(len(lst) / 2)):
    answer = min(answer, lst[i:i + a].count('b'))
print(answer)
