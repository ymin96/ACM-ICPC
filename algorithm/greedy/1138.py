n = int(input())

inputList = list(map(int, input().split()))

answer = [0 for _ in range(n)]

for i in range(n):
    idx = 0
    cnt = inputList[i]
    while cnt > 0 or answer[idx] != 0:
        if answer[idx] == 0:
            cnt -= 1
        idx += 1
    answer[idx] = i + 1

for i in answer:
    print(i, end=" ")