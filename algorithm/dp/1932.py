n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
for i in range(n - 2, -1, -1):
    for j in range(len(lst[i])):
        lst[i][j] = lst[i][j] + max(lst[i + 1][j], lst[i + 1][j + 1])
print(lst[0][0])
