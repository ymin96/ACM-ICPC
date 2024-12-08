N, K = map(int, input().split())
lst = []

for i in range(N):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: (-x[1], -x[2], -x[3]))
for i in range(N):
    lst[i].append(i + 1)
for i in range(1, N):
    if lst[i - 1][1:-1] == lst[i][1:-1]:
        lst[i][4] = lst[i - 1][4]
for country in lst:
    if country[0] == K:
        print(country[4])
