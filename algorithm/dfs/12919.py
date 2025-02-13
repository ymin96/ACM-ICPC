import sys

check = False
def DFS(S, T):
    global check
    if S == T:
        check = True
        return
    elif len(T) <= len(S):
        return
    if not check:
        if T[-1] == "A":
            DFS(S, T[:-1])
        if T[0] == "B":
            T = T[1:]
            DFS(S, T[::-1])

    return


S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()
DFS(S, T)
if check:
    print(1)
else:
    print(0)
