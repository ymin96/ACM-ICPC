from itertools import permutations

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
lst = list(permutations(lst, m))
for element in lst:
    for i in element:
        print(i, end=" ")
    print()
