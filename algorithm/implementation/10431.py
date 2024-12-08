import sys

P = int(sys.stdin.readline().rstrip())

for k in range(P):
    lst = list(map(int, sys.stdin.readline().rstrip().split()))
    length = [-1 for i in range(20)]
    ans = 0
    for i in range(1, 21):
        num = lst[i]
        for j in range(19, 0, -1):
            if length[j-1] == -1:
                length[j] = length[j - 1]
                length[j - 1] = num
            elif length[j - 1] > num:
                length[j] = length[j - 1]
                length[j - 1] = num
                ans += 1
    print(str(k + 1) + " " + str(ans))
