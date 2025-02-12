import sys

N = int(sys.stdin.readline().strip())

lst = []
upper = []
for i in range(N):
    lst.append(sys.stdin.readline().strip())
    upper.append(lst[i].upper())

scanLst = []
checkLst = [0 for i in range(ord('Z') - ord('A') + 1)]
index = [-1 for i in range(N)]
for i in range(N):
    scan = ""
    option = upper[i]
    optionSplit = option.split()
    check = True
    for j in optionSplit:
        if checkLst[ord(j[0]) - ord('A')] == 0:
            checkLst[ord(j[0]) - ord('A')] = 1
            index[i] = option.index(j)
            check = False
            break
    if check:
        for j in range(len(option)):
            if option[j] != " " and checkLst[ord(option[j]) - ord('A')] == 0:
                checkLst[ord(option[j]) - ord('A')] = 1
                index[i] = j
                break

for i in range(N):
    for j in range(len(lst[i])):
        if j == index[i]:
            print("[" + lst[i][j] + "]", end="")
        else:
            print(lst[i][j], end="")
    print()
