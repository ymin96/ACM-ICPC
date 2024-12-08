import sys

M = int(input())
S = [0 for i in range(21)]
for i in range(M):
    lst = list(sys.stdin.readline().rstrip().split())
    order = lst[0]
    if order == "add":
        S[int(lst[1])] = 1
    elif order == "remove":
        S[int(lst[1])] = 0
    elif order == "check":
        sys.stdout.write("1\n") if S[int(lst[1])] == 1 else sys.stdout.write("0\n")
    elif order == "toggle":
        if S[int(lst[1])] == 1:
            S[int(lst[1])] = 0
        else:
            S[int(lst[1])] = 1
    elif order == "all":
        S = [1 for i in range(21)]
    elif order == "empty":
        S = [0 for i in range(21)]
