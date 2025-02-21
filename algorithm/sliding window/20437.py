import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    W = sys.stdin.readline().strip()
    K = int(sys.stdin.readline().strip())
    maxNum = 10000001
    minNum = -1
    maxAns = minNum
    minAns = maxNum

    lst = [0 for i in range(26)]
    for i in W:
        lst[ord(i) - ord('a')] += 1

    if K == 1:
        print("1 1")
        continue

    for i in range(len(W)):
        if lst[ord(W[i]) - ord('a')] >= K:
            temp = 1
            for j in range(i + 1, len(W)):
                if W[j] == W[i]:
                    temp += 1
                if temp == K:
                    maxAns = max(maxAns, j - i + 1)
                    minAns = min(minAns, j - i + 1)
                    break

        lst[ord(W[i]) - ord('a')] -= 1

    if maxAns == minNum:
        print(-1)
    else:
        print(str(minAns) + " " + str(maxAns))
