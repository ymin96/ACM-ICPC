import sys

def binary_search(search_lst, n):
    low = 0
    high = len(search_lst)
    while low < high:
        mid = (low + high) // 2
        if search_lst[mid][1] < n:
            low = mid + 1
        else:
            high = mid
    return search_lst[high][0]


N, M = map(int, sys.stdin.readline().strip().split())

lst = []
for i in range(N):
    title, point = sys.stdin.readline().strip().split()
    lst.append([title, int(point)])
searchLst = []
for i in range(M):
    search = int(sys.stdin.readline().strip())
    searchLst.append(binary_search(lst,search))

for i in searchLst:
    print(i)