N = int(input())
M = int(input())
light = list(map(int, input().split()))
low = 1
high = N
ans = 1000001
while low <= high:
    mid = int(low + (high - low) / 2)
    lst = []
    for i in light:
        lst.append(i - mid)
        lst.append(i + mid - 1)
    check = 1
    if 0 >= lst[0] and N - 1 <= lst[-1]:
        check = -1
        for i in range(1, len(lst), 2):
            if i < len(lst) - 1 and lst[i + 1] - lst[i] > 1:
                check = 1
                break
        if check == -1:
            ans = min(ans, mid)
    if check > 0:
        low = mid + 1
    else:
        high = mid - 1
print(ans)
