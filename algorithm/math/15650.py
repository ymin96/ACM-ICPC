from itertools import combinations

n, m = map(int, input().split())
lst = [i for i in range(1, n + 1)]
lst = list(combinations(lst, m))
for element in lst:
    for i in element:
        print(i, end=" ")
    print()