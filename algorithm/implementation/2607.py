import copy
import sys

N = int(sys.stdin.readline().strip())
mWord = sys.stdin.readline().strip()
lst = [0 for _ in range(0, ord('Z') - ord('A')+1)]
for ch in mWord:
    lst[ord(ch) - ord('A')] += 1

sWords = []
ans = 0

for i in range(N - 1):
    sWords.append(sys.stdin.readline().strip())

for word in sWords:
    if abs(len(mWord) - len(word)) < 2:
        tmpLst = copy.deepcopy(lst)
        for ch in word:
            tmpLst[ord(ch) - ord('A')] -= 1
        p, m = 0, 0
        for i in tmpLst:
            if i > 0:
                p += abs(i)
            elif i < 0:
                m += abs(i)
        if p <= 1 and m <= 1:
            ans += 1
print(ans)
